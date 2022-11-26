"""Create view for reading fiction's story."""
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import requires_csrf_token
from fiction_fans.models import FictionTitle, FictionChapter

# Create your views here.


class ChapterView(generic.DetailView):
    """Create view for reading fiction's chapter page."""
    template_name = "fiction_fans/chapter_page.html"
    model = FictionChapter

    def get_queryset(self):
        fiction_pk = self.kwargs.get("fiction_pk")
        return FictionTitle.objects.filter(pk=fiction_pk)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        chapter_pk = self.kwargs.get("chapter_pk")
        queryset = FictionChapter.objects.filter(pk=chapter_pk)
        return queryset.get()


def fiction_view(request, fiction_id):
    """Create view of fiction for show fiction's title and list of episode."""
    template_name = "fiction_fans/fiction_page.html"
    fiction = FictionTitle.objects.get(id=fiction_id)
    chapters = fiction.fictionchapter_set.all()
    context = {
        "fiction": fiction,
        "chapters": chapters
    }
    return render(request, template_name, context=context)


@requires_csrf_token
def upload_image_view(request):
    file_request = request.FILES["image"]
    file_system = FileSystemStorage()
    filename = str(file_request).split(".")[0]
    file = file_system.save(filename, file_request)
    file_url = file_system.url(file)
    return JsonResponse(
        {
            "success": 1,
            "file": {"url": file_url},
        }
    )
