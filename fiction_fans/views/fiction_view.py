"""Create view for reading fiction's story."""
from django.shortcuts import render
from ..models.fiction_model import FictionTitle ,FictionChapter
from django.views import generic

# Create your views here.

class ChapterView(generic.DetailView):
    """Create view for reading fiction's chapter page."""
    template_name = "fiction_fans/chapter_page.html"
    model = FictionChapter

    def get_queryset(self):
        pk = self.kwargs.get("title_pk")
        return FictionTitle.objects.filter(pk=pk)
    
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        pk = self.kwargs.get('chapter_pk')
        queryset = FictionChapter.objects.filter(pk=pk)
        return queryset.get()
        
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
