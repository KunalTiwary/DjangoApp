from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Project as pro
from wikipediaapi import Wikipedia
from sentence.models import Sentence as sen
from django.contrib.auth.models import User


@login_required
def project(request):
    # Each request is first a get request which goes in the elif part first which renders project.html and the html file
    # again calls this function with a post request.
    annotators = []
    # getting all users
    users = User.objects.all()
    for user in users:
        # getting annotators
        if checkAnnotator(user):
            annotators.append(user)
    # considering all the groups(annotator and manager) and making a set of it to save traverse time complexity
    groupsQ = request.user.groups.all()
    groups = set()
    for group in groupsQ:
        groups.add(group.name)
    # if the user is logged in, belongs to manager group and the request is a post request
    if request.user.is_authenticated and "Manager" in groups and request.method == 'POST':
        wikiTitle = request.POST.get('wikiTitle')
        targetLang = request.POST.get('targetLang')
        annotator = request.POST.get('annotator')
        pr = pro(articleTitle=wikiTitle, targetLanguage=targetLang, annotator=annotator)
        # saving the details given by user to the database
        pr.save()
        # obtaining the summary of the article, splitting it and storing in sentences table
        summary = Wikipedia().page(wikiTitle).summary
        sentences = summary.split('. ')
        for i, sentence in enumerate(sentences):
            s = sen(projectId=pr, sentenceId=i + 1, originalSentence=sentence)
            s.save()
        return HttpResponseRedirect('/projectcreated')
    elif request.user.is_authenticated and "Manager" in groups:
        return render(request, 'project.html', {'users': annotators})
    else:
        # if an annotator tries to create a project by directly calling the url /project.
        return render(request, 'notAuthorised.html')

# after project created
@login_required
def projectCreated(request):
    if request.method == 'GET':
        return render(request, 'created.html')

# helper function of project
def checkAnnotator(user):
    groupsQ = user.groups.all()
    groups = set()
    for group in groupsQ:
        groups.add(group.name)
    if "Annotator" in groups:
        return True
    return False

@login_required
def listProjects(request):
    # considering all the groups(annotator and manager) and making a set of it to save traverse time complexity
    groupsQ = request.user.groups.all()
    groups = set()
    for group in groupsQ:
        groups.add(group.name)
    # if the user is logged in and is manager we let the user view all projects
    if request.user.is_authenticated and "Manager" in groups:
        projects = pro.objects.all()
        return render(request, 'listProjects.html', {'projects': projects})
    # if the user is logged in and is annotator we let the user view only those projects assigned to him/her.
    elif request.user.is_authenticated and "Annotator" in groups:
        # getting all projects
        projects = []
        allProjects = pro.objects.all()
        for project in allProjects:
            # getting all the projects assigned to that user
            if project.annotator == request.user.username:
                projects.append(project)
        return render(request, 'listAnnotatorProjects.html', {'projects': projects})
    else:
        return render(request, 'notAuthorised.html')