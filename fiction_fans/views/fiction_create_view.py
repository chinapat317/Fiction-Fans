from django.shortcuts import render, redirect
from django.urls import reverse
from .homepage_view import HomePage
# from .fiction_view import fiction_view, ChapterView
from ..forms.fiction_form import FictionForm, ChapterForm
from ..models.fiction_model import FictionTitle, FictionChapter

# Create your views here.


def create_fiction(request):
    form = FictionForm(request.POST or None)
    template_name = "fiction_fans/fiction_create.html"
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/fiction/")
    return render(request, template_name, context=context)


def create_chapter(request):
    form = ChapterForm(request.POST or None)
    template_name = "fiction_fans/chapter_create.html"
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/fiction/")
    return render(request, template_name, context=context)
