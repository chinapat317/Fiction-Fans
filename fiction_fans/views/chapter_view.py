from ..models import FictionChapter
from django.views import generic

# Create your views here.

class ChapterView(generic.DetailView):
    """Class based view for viewing story"""
    template_name = "/chapter_page.html"
    model = FictionChapter
