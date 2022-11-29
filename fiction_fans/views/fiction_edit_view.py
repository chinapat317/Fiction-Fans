"""Edit feature for fiction and chapter."""
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from ..forms.fiction_form import FictionForm, ChapterForm
from ..models.fiction_model import FictionTitle, FictionChapter
from . import storage

# Create your views here.


def edit_fiction(request, fiction_id):
    """
    Edit fiction on edit fiction page by using form
    to save information from writer.
    """
    fiction = get_object_or_404(FictionTitle, id=fiction_id)
    form = FictionForm(request.POST or None, instance=fiction)
    template_name = "fiction_fans/fiction_edit.html"
    context = {
        "fiction": fiction,
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/fiction/{}/".format(fiction.id))
    return render(request, template_name, context=context)


def edit_chapter(request, fiction_id, chapter_id):
    """
    Edit chapter on edit chapter page by using form
    to save information from writer.
    """
    fiction = FictionTitle.objects.get(id=fiction_id)
    chapter = get_object_or_404(FictionChapter, id=chapter_id)
    form = ChapterForm(request.POST or None, instance=chapter)
    template_name = "fiction_fans/chapter_edit.html"
    context = {
        "chapter": chapter,
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                "/fiction/{}/{}/".format(fiction.id, chapter.id)
            )
    return render(request, template_name, context=context)
