from django_editorjs import EditorJsField
from django.db import models

class Story(models.Model):
    ''' Model for creating story.'''
    title = models.CharField(max_length=50)
    body = EditorJsField()


