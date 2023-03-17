import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from project.models import project as pro
from .models import Sentence
# Create your views here.


def sentence(request, projectId):
    if request.method == 'POST':
        translations = json.loads(request.body)
        for translation in translations:
            originalSentence = translation['originalSentence']
            translatedSentence = translation['translatedSentence']
            p = pro.objects.get(id=projectId)
            sen = Sentence.objects.get(projectId=p, originalSentence=originalSentence)
            sen.translatedSentence = translatedSentence
            sen.save()
        return HttpResponseRedirect('/sentenceupdated')
    project = pro.objects.get(id=projectId)
    sentences = Sentence.objects.filter(projectId=project)
    return render(request, 'sentences.html', {'sentences': sentences, 'project': project})


def sentenceUpdated(request):
    if request.method == 'GET':
        return render(request, 'sentenceUpdated.html')
