from django.db import models
from Projects.models import Project

# Create your models here.
class Sentence(models.Model):
    sentence_ID = models.IntegerField(max_length=100, primary_key=True)
    original_string = models.CharField(max_length=10000)
    translated_string = models.CharField(max_length=10000)
    project_ID = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
