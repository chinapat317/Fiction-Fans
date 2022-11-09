from django.forms import ModelForm
from ..models.fiction_model import FictionTitle, FictionChapter


class FictionForm(ModelForm):
    class Meta:
        model = FictionTitle
        fields = "__all__"


class ChapterForm(ModelForm):
    class Meta:
        model = FictionChapter
        fields = ["title", "content", "fiction_title"]
