from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm ,ProfileUpdateForm

def logout_view(request):
    logout(request)
    # return HttpResponseRedirect(reverse('login'))
    return render(request,"stackusers/logout.html")



def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Account Successfully created for {username}. Log In Now !!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'stackusers/register.html', {'form': form})

@login_required

def profile(request):
    return render(request, 'stackusers/profile.html')

@login_required
def profile_update(request):
    if request.method == "POST":
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            # .is_valid() kya check krta hai?
            p_form.save()
            u_form.save()
            messages.success(request,f"Your profile is updated")  # i want to add username in the string
            return redirect("profile")

    else:
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

    context={
        "u_form":u_form,
        "p_form":p_form
        }

    return render(request,"stackusers/profile_update.html", context)

# abhi pehle se likh ke aane lge the update wale form mein credentials but ab chle gye jab indentation shi kra tab kuch toh hua hai



# Problem
'''
ek baar form update kr rha hu uske baad go back wala button kaam ni kr
rha hai bo dekhna pdega mujhe


ab kaam krne lg gya waps se server abhi restart hua tha , toh sayd glitch hua hoga ab shi ho gya .

message wala aur kr du jra


'''

















# error dene wala code

# Create your views here.
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid(): 
#             # credentials agr shi hai username aur wageraa
#             form.save()
#             username = form.cleaned_data.get("username")
#             return redirect("home")
        
#         else:
#             form=UserCreationForm()

#         return render(request,"stackusers/register.html",{'form': form})
