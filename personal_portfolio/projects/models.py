from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technolodgy=models.CharField(max_length=100)
    image=models.FilePathField(path="/img")
    urls=models.URLField()
