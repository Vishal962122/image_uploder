from django.db import models

# Create your models here.
class Image(models.Model ):
    photov=models.ImageField(upload_to="myimage")
    date= models.DateTimeField(auto_now_add=True)