from django.shortcuts import render, get_object_or_404
from .homepage_view import HomePage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from fiction_fans.models import FictionTitle, FictionChapter

# Create your views here.


def delete_fiction(request, fiction_id):
    fiction = get_object_or_404(FictionTitle, id=fiction_id)
    template_name = "fiction_fans/fiction_delete.html"
    context = {
        "fiction": fiction,
    }
    if request.method == "POST":
        fiction.delete()
        return HttpResponseRedirect("/fiction/")
    return render(request, template_name, context=context)


def delete_chapter(request, fiction_id, chapter_id):
    fiction = FictionTitle.objects.get(id=fiction_id)
    chapter = get_object_or_404(FictionChapter, id=chapter_id)
    template_name = "fiction_fans/chapter_delete.html"
    context = {
        "fiction": fiction,
        "chapter": chapter,
    }
    if request.method == "POST":
        chapter.delete()
        return HttpResponseRedirect("/fiction/{}/".format(fiction.id))
    return render(request, template_name, context=context)
