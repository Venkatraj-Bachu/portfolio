from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    gitlink = models.URLField(blank=True)
    projectlink = models.URLField(blank=True)
    image = models.ImageField()
