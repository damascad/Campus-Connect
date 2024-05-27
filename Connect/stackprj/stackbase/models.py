from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# from tinymce.models import HTMLField
# from ckeditor_uploader.fields import RichTextField
# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title= models.CharField(max_length=10000)
    content=models.TextField(null =True, blank=True)
    # content = RichTextField()
    likes=models.ManyToManyField(User, related_name="question_post")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - Question"
    
    def get_absolute_url(self):
        return reverse("stackbase:question-detail", kwargs={"pk": self.pk})
    # upar wali line itna kh ri hai ki bas jab question post krne ke baad question-detail wale url mein jo primary
# se create hua hai question wahi kholke de dena 
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    question=models.ForeignKey(Question,related_name="comment", on_delete=models.CASCADE) 
# upar wali line question model ko pura inherit kr ri tabhi mein neeche question model ki cheezein use kr paa rha?
    name=models.CharField(max_length=100)
    content=models.TextField(null=True,blank=True)
    # content= RichTextField()
    date_created=models.DateTimeField(default=timezone.now)

    def __str__(self): # ye database mein heading kaise show hogi bo
        return "%s - %s" %(self.question.title , self.question.user)
    
    def get_absolute_url(self):
        return reverse("stackbase:question-detail", kwargs={"pk": self.pk})
    
    def save(self , *args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-date_created'] 
        # yha ise humne order mein laa diya time ke hisaab se.
        # ye save function exactly save kr rha comment ? agr haa toh .... pata krna hai thoda iske baare mein.




# polls

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
    def __str__(self):
        return f"{self.question}"
    class Meta:
        ordering = ['-date_created'] 