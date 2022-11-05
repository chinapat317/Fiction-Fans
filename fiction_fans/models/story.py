from django_editorjs import EditorJsField
from django.db import models
from django.utils import timezone

class Story(models.Model):
    ''' Model for creating story.'''
    title = models.CharField(max_length=50)
    body = EditorJsField()
    pub_date = models.DateTimeField(auto_now_add=True)
    


