from django.contrib import admin
from .models.fiction_model import FictionTitle, FictionChapter

# Register your models here.

admin.site.register(FictionChapter)
admin.site.register(FictionTitle)
