from django.db import models


# Create your models here.
class Project(models.Model):
    article_title = models.CharField(max_length=100)
    target_language = models.CharField(max_length=100)
    # print(article_title, target_language)
    project_ID = models.CharField(max_length=255, unique=True,  # default=str(target_language)+"_"+str(article_title),
                                  primary_key=True)
