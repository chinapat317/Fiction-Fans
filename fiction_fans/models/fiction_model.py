from django.db import models
from django.utils import timezone
from django_editorjs import EditorJsField

# Create your models here.
    
class FictionTitle(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class FictionChapter(models.Model):
    title = models.CharField(max_length=255)
    content = EditorJsField()
    novel_title = models.ForeignKey(NovelTitle, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} is chapter of {self.novel_title}"
