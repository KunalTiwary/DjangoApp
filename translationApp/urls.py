"""translationApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.urls import path
from sentence.views import sentence, sentenceUpdated

from project.views import project, projectCreated, listProjects


class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/listprojects/'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', project, name='project'),
    path('projectcreated/', projectCreated, name='projectcreated'),
    path('sentences/<int:projectId>/', sentence, name='sentences'),
    path('sentenceupdated/', sentenceUpdated, name='sentenceupdated'),
    path('listprojects/', listProjects, name='listprojects'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', CustomLoginView.as_view(), name='login'),
]
