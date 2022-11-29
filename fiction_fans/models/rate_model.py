"""Rate model for each chapter in fiction."""
from django.db import models
from django.conf import settings
from .fiction_model import FictionChapter

# Create your models here.


class RateModel(models.Model):
    """Get rate score of the chapter by the user."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chapter = models.ForeignKey(FictionChapter, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
