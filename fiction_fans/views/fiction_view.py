"""Create view for reading fiction's story."""
from django.shortcuts import render
from ..models.fiction_model import FictionTitle ,FictionChapter
# from django.views import generic

# Create your views here.

# class ChapterView(generic.DetailView):
#     """Create view for reading fiction's chapter page."""
#     template_name: str = "/chapter_page.html"
#     model = FictionChapter

def fiction_view(request, fiction_id):
    """Create view of fiction for show fiction's title and list of episode."""
    template_name = "fiction_page.html"
    fiction = FictionTitle.objects.get(id=fiction_id)
    chapters = FictionChapter.objects.filter(fiction_title=fiction)
    context = {
        "fiction": fiction,
        "chapters": chapters,
    }
    return render(request, template_name, context=context)


def chapter_view(request, fiction_id, chapter_id):
    """Create view of chapter for show chapter's title and content in that chapter."""
    template_name = "chapter_page.html"
    fiction = FictionTitle.objects.get(id=fiction_id)
    chapter = FictionChapter.objects.get(id=chapter_id)
    context = {
        "fiction": fiction,
        "chapter": chapter,
    }
    return render(request, template_name, context=context)
