from django.contrib import admin
from .models import FictionTitle, FictionChapter

# Register your models here.
admin.site.register(FictionChapter)
admin.site.register(FictionTitle)