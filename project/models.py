from django.db import models


# Create your models here.
class Project(models.Model):
    # id will be taken automatically
    articleTitle = models.CharField(max_length=100)
    targetLanguage = models.CharField(max_length=100)
    annotator = models.CharField(max_length=100, default="kunal")