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
    groupsQ = request.user.groups.all()
    groups = set()
    for group in groupsQ:
        groups.add(group.name)
    # if the method is post and if the user is that project's annotator, the second check is necessary only in that
    # case when the user knows some project id and is trying to go through some other annotator's project through URL.
    # Also, if the user is a manager he can access all the sentences and change it.
    if request.method == 'POST' and (p.annotator == request.user.username or "Manager" in groups):
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
    elif p.annotator == request.user.username or "Manager" in groups:
        project = pro.objects.get(id=projectId)
        sentences = Sentence.objects.filter(projectId=project)
        return render(request, 'sentences.html', {'sentences': sentences, 'project': project})
    else:
        return render(request, 'notAuthorised.html')

# after updating
@login_required
def sentenceUpdated(request):
    if request.method == 'GET':
        return render(request, 'sentenceUpdated.html')
