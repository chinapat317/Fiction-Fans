from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from ..forms.fiction_create_form import FictionForm, ChapterForm


def create_fiction(request):
    """
    For creating fiction title page.
    """
    form = FictionForm(request.POST or None)
    template_name = "fiction_fans/fiction_create.html"
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            fiction = form.save()
            return HttpResponseRedirect(reverse("fiction_fans:fiction_view", args=(fiction.id,)))
    return render(request, template_name, context=context)


def create_chapter(request):
    """
    For creating chapter in fiction title.
    """
    form = ChapterForm(request.POST or None)
    template_name = "fiction_fans/chapter_create.html"
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            chapter = form.save()
            fiction_pk = chapter.fiction_title_id
            chapter_pk = chapter.id
            return HttpResponseRedirect(reverse("fiction_fans:chapter_view", args=[fiction_pk, chapter_pk]))
    return render(request, template_name, context=context)
