"""Rate feature for chapter of the fiction."""
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from fiction_fans.models import RateModel, FictionChapter

# Create your views here.


def rate(request, fiction_pk, chapter_pk):
    """
    Rate feature for chapter of fiction.
    User must logged in to rate the chapter, otherwise
    user get error message and redirect to login page.
    """
    user = request.user
    if not user.is_authenticated:
        messages.add_message(
            request, messages.INFO,
            "Please login before rating."
        )
        return HttpResponseRedirect("../../../../accounts/login/")
    chapter = get_object_or_404(FictionChapter, pk=chapter_pk)
    point = request.POST.get("point")
    try:
        rate = RateModel.objects.get(user=user, chapter=chapter_pk)
        rate.point = point
    except:
        rate = chapter.ratemodel_set.create(user=user, point=point)
    rate.save()
    return HttpResponseRedirect(
        reverse("fiction_fans:chapter_view",
        args=[fiction_pk, chapter_pk])
    )
