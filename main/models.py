import view as view
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=124)
    post = models.TextField()
    date = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to="gallery")


class Image(models.Model):
    title = models.CharField(max_length=124)
    picture = models.ImageField(upload_to="gallery")
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
