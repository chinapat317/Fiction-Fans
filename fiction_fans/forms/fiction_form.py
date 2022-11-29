"""Form for creating and editing Fiction and Chapter models."""
from django.forms import ModelForm
from ..models.fiction_model import FictionTitle, FictionChapter


class FictionForm(ModelForm):
    class Meta:
        model = FictionTitle
        fields = [
            "title",
            "author",
            "translator",
            "status",
            "description",
        ]


class ChapterForm(ModelForm):
    class Meta:
        model = FictionChapter
        fields = ["title", "content"]
