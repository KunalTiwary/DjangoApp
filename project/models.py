from django.db import models

# Create your models here.
class project(models.Model):    #######################capital
    articleTitle = models.CharField(max_length=100)
    targetLanguage = models.CharField(max_length=100)