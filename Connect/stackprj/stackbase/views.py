from django.forms import forms 
from .forms import CreatePollForm
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse_lazy 
from django.views.generic import ListView,DetailView,CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin , LoginRequiredMixin
from .models import Question , Comment , Poll
from .forms import CommentForm
from django.shortcuts import render, redirect

# Create your views here.
opera = Question.id
def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")

# views mein pehli baar class banaya hai

# CRUD function
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    # upar wali line kah ri hai jo bhi iss class mein hai bo iss questions variable mein daal do
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context
def like_view(request, pk):
    post = get_object_or_404(Question, id=request.POST.get('question_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse_lazy('stackbase:question-detail', args=[str(pk)]))

class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        something = get_object_or_404(Question, id=self.kwargs['pk'])
        total_likes = something.total_likes()
        liked = False
        if something.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class QuestionCreateView(LoginRequiredMixin,CreateView):
    model=Question
    fields =  ["title","content"]
    def form_valid(self,form):
        form.instance.user=self.request.user # jo user login hai wahi bhej paayega question
        return super().form_valid(form) # ye line databse mein add kraegi sayd hamara question.

class QuestionUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Question
    fields =  ["title","content"]
    
    # def form_valid(self,form):
    #     form.instance.user=self.request.user # jo user login hai wahi bhej paayega question
    #     return super().form_valid(form)
    
    # ye wala form_valid function create ke liye likha toh ha aur ye interconnectrd hai aur ek hi template use kr rha toh 2 baar likh ke fayda ni kaam thik se kr rha hai aise toh . toh mein comment kr de rha hu ok.
    # UserPassesTestMixin ye use krne ke le liye aapko test_func() banana pdega
    def test_func(self):
        questions=self.get_object() #.get_object() function hai berrroooo ise call kra kro , mein call ni kr rha rha itni der se bas naam likh ke chor rkha tha aur error khaa rha tha waooo.
        
        if self.request.user == questions.user:
            
            return True 
        return False


class QuestionDeleteView(UserPassesTestMixin , LoginRequiredMixin,DeleteView):
    model= Question
    # success_url = "stackbase:home"  #yha pr hi le rha bo success url button ko href de rha toh kaam ni kr rha 
    success_url=reverse_lazy("stackbase:question-list")
    def test_func(self):
        questions=self.get_object()
        
        if self.request.user == questions.user:
            
            return True 
        else:
            return False
        

'''
error ka solution
error : 

DisallowedRedirect at /questions/3/delete
Unsafe redirect to URL with protocol 'stackbase'

solution:

The error you're encountering is due to the incorrect format of the success_url attribute in your QuestionDeleteView. Instead of providing the URL name directly, you should use the reverse_lazy function to dynamically resolve the URL name to its actual URL.

Here's the corrected version of your QuestionDeleteView:

'''



class CommentDetailView(LoginRequiredMixin,CreateView):
    model=Comment
    form_class= CommentForm #ye form_class hamari forms,py se template uthayegi aur jis jgh assign kroge waha waha bo kaam kregi vaise jaise btaoge abhi toh create view ki jha redirecting hogi wahi se template uthayega ok.
    success_url="stackabse/question_detail.html"
    
    # ab yha form valid method to get valid response from the form and save it in databse
    # ye form wala argument khi define ni hai but ja kaise rha?
    def form_valid(self,form):
        form.instance.question_id=self.kwargs["pk"]
        return super().form_valid(form)
        
    success_url= reverse_lazy("stackabse:question-detail")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(question_id=self.kwargs["pk"]).order_by('date_created')
        context['comments'] = comments
        return context


class AddComment(LoginRequiredMixin,CreateView):
    model=Comment
    form_class=CommentForm
    template_name="stackbase/question_answer.html"

    def form_valid(self,form):
        form.instance.question_id=self.kwargs["pk"]
        return super().form_valid(form)
    # success_url= reverse_lazy("stackbase:question-detail", kwargs={'pk': self.request.opera}) #if i can pass the id of the question.id model with this 
    # success_url= reverse_lazy("stackbase:question-detail")
    def get_success_url(self):
        return reverse_lazy("stackbase:question-detail", kwargs={'pk': self.kwargs["pk"]}) #but ye thik kaam kr rha
        # return reverse_lazy("stackbase:question-detail", kwargs={'pk': self.opera}) opera wala trika mein dekhunga ji abhi ismein problem hai ye kaam ni kr rha thik se .



        # 

# def polls(request):
#     return render(request,"polls.html")
def goodies(request):
    return render(request,"goodies.html")



# polls





def list(request):
    polls = Poll.objects.all()
    ordering = ['-date_created']
    context = {
        'polls' : polls
    }
    return render(request, 'stackbase/list.html', context)

# def create(request):
#     if request.method == 'POST':
#         form = CreatePollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = CreatePollForm()
#     context = {
#         'form' : form
#     }
#     return render(request, 'create.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('stackbase:poll_results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'stackbase/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'stackbase/results.html', context)

