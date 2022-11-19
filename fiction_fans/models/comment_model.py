from django.db import models
from .fiction_model import FictionChapter

class Comment(models.Model):
    """Create comment in chapter and keep it in sqlite."""
    chapter = models.ForeignKey(FictionChapter, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    text = models.CharField(max_length=255)