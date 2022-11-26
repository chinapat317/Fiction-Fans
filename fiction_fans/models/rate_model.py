from django.db import models
from django.conf import settings
from .fiction_model import FictionChapter

class RateModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chapter = models.ForeignKey(FictionChapter, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    

