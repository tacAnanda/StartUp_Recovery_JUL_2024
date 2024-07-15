from django.db import models



# Create your models here.


class USER_INFO(models.Model):
    userName = models.CharField(max_length=200)
    userImage=models.ImageField(upload_to='User_Info_Image/')
    
    
    
