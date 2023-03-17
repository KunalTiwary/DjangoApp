from django.db import models
from project.models import project

class Sentence(models.Model):
    projectId = models.ForeignKey(project, on_delete=models.CASCADE)
    sentenceId = models.IntegerField()
    originalSentence = models.CharField(max_length=500)
    translatedSentence = models.CharField(max_length=500, null=True)

