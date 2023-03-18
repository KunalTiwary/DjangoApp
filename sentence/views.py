import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from project.models import Project as pro
from .models import Sentence
# Create your views here.

@login_required
def sentence(request, projectId):
    # getting the project object from id
    p = pro.objects.get(id=projectId)
    # if the method is post and if the user is that project's annotator, the second check is necessary only in that
    # case when the user knows some project id and is trying to go through some other annotator's project through URL.
    if request.method == 'POST' and p.annotator == request.user.username:
        # all the translations given by user is given to request body which is unpacked and saved here.
        translations = json.loads(request.body)
        for translation in translations:
            originalSentence = translation['originalSentence']
            translatedSentence = translation['translatedSentence']
            sen = Sentence.objects.get(projectId=p, originalSentence=originalSentence)
            sen.translatedSentence = translatedSentence
            sen.save()
        return HttpResponseRedirect('/sentenceupdated')
    # for get request
    elif p.annotator == request.user.username:
        project = pro.objects.get(id=projectId)
        sentences = Sentence.objects.filter(projectId=project)
        return render(request, 'sentences.html', {'sentences': sentences, 'project': project})
    else:
        return HttpResponse("<h1>Not Authorised</h1>")

# after updating
@login_required
def sentenceUpdated(request):
    if request.method == 'GET':
        return render(request, 'sentenceUpdated.html')
