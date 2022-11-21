from django.db import models
from .fiction_model import FictionChapter
from django.conf import settings

class Comment(models.Model):
    """Create comment in chapter and keep it in sqlite."""
    chapter = models.ForeignKey(FictionChapter, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)