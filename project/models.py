from django.db import models
from django.urls import path

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img") # all images of the site is saved here
    date_created = models.DateTimeField(auto_now_add=True) #to add current date and time to our project

    def __str__(self) -> str:
        return self.title