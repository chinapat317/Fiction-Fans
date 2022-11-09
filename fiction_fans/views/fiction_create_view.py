from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from ..forms.fiction_form import FictionForm, ChapterForm

# Create your views here.


def create_fiction(request):
    form = FictionForm(request.POST or None)
    template_name = "fiction_fans/fiction_create.html"
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            fiction = form.save()
            return HttpResponseRedirect(reverse("fiction_view", args=(fiction.id,)))
    return render(request, template_name, context=context)


def create_chapter(request):
    form = ChapterForm(request.POST or None)
    template_name = "fiction_fans/chapter_create.html"
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            chapter = form.save()
            return HttpResponseRedirect(reverse("chapter_view", args=(chapter.novel_title.id, chapter.id,)))
    return render(request, template_name, context=context)
