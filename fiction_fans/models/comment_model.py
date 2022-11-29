"""Model for comment on chapter page."""
from django.db import models
from django.conf import settings
from django.utils import timezone
from .fiction_model import FictionChapter

# Create your models here.


class Comment(models.Model):
    """
    Create comment model in chapter
    and keep it in sqlite with timestamp.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    chapter = models.ForeignKey(FictionChapter, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=timezone.now())
