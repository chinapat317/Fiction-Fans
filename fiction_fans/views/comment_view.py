"""Comment view for comment feature."""
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import FictionChapter
from django.urls import reverse

# Create your views here.


def comment(request, fiction_pk, chapter_pk):
    """
    User comment on chapter page, user cannot comment
    if not logged in. Redirect user to login page.
    """
    user = request.user
    if not user.is_authenticated:
        messages.add_message(request, messages.INFO, "Please login before comment.")
        return HttpResponseRedirect("../../../../accounts/login/")
    chapter = get_object_or_404(FictionChapter, pk=chapter_pk)
    comment_text = request.POST.get("comment_text")
    #################################################################
    # delete when finish
    file = open("log.txt", "w")
    file.write("comment_text = {}".format(request.POST.get("comment_text")))
    file.close
    ###################################################################
    chapter.comment_set.create(user=user, text=comment_text)
    return HttpResponseRedirect(
        reverse("fiction_fans:chapter_view",
        args=[fiction_pk, chapter_pk])
    )
