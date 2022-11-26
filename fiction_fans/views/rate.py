from fiction_fans.models import RateModel, FictionChapter
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse

def rate(request, fiction_pk, chapter_pk):
    user = request.user
    if not user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Please login before rate.')
        return HttpResponseRedirect('../../../../accounts/login/')
    chapter = get_object_or_404(FictionChapter, pk=chapter_pk)
    point = request.POST.get('point')
    ######################################
    # delete when finish
    file = open("log.txt", "w")
    file.write("point = {}".format(point))
    file.close()
    ################################
    try:
        rate = RateModel.objects.get(user=user, chapter=chapter_pk)
        rate.point = point
    except:
        rate = chapter.ratemodel_set.create(user=user, point=point)
    rate.save()
    return HttpResponseRedirect(reverse('fiction_fans:chapter_view', args=[fiction_pk, chapter_pk]))