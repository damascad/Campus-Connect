from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.CharField(max_length=1000)
    phone=models.IntegerField(null=True, blank=True)
    # upar wali line bata ri hai ki ek user ek hi profile create kr paaye
    image=models.ImageField(default="default.png", upload_to="profile_pic")


    def __str__(self):
        return f"{self.user.username} - Profile"
    
# to resize the image and store it on that location where it founds from ok.

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img= Image.open(self.image.path)
        if(img.height >300 or img.width >300):
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path,format="PNG")