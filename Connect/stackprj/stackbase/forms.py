from .models import Comment ,Poll
from django import forms
from django.forms import ModelForm

class CommentForm(forms.ModelForm):
    #mujhe thoda idea toh lg rha hai naam dekh ke ki ye arguent kaam kaise karta hai but actually iska content documentation mein check krunga , if i did further work in web development
    
    class Meta:
        model=Comment
        fields=["name","content"]


# yha hum html ni django ke inbulit cheez form ka use kr re widgets dictionary mein
        widegts={
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "body": forms.Textarea(attrs={"class":"form-control"}),
        }



class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']