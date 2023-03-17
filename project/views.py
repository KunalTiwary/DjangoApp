from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import project as pro
from wikipediaapi import Wikipedia
from sentence.models import Sentence as sen

def project(request):
    if request.method == 'POST':
        wikiTitle = request.POST.get('wikiTitle')
        targetLang = request.POST.get('targetLang')
        pr = pro(articleTitle=wikiTitle, targetLanguage=targetLang)
        pr.save()
        summary = Wikipedia().page(wikiTitle).summary
        sentences = summary.split('. ')
        for i, sentence in enumerate(sentences):
            s = sen(projectId=pr, sentenceId=i + 1, originalSentence=sentence)   ####sentence id
            s.save()
        return HttpResponseRedirect('/projectCreated')
    else:
        return render(request, 'project.html')


def projectCreated(request):
    if request.method == 'GET':
        return render(request, 'created.html')


def listProjects(request):
    projects = pro.objects.all()
    return render(request, 'listProjects.html', {'projects': projects})