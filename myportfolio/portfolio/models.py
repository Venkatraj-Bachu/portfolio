from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    gitlink = models.URLField(blank=True)
    projectlink = models.URLField(blank=True)
    image = models.ImageField()

class ContactMe(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()