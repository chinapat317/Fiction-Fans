from django.views import generic

# importing module
import sys

# appending a path
sys.path.append('../models')

from story import Story

# Create your views here.


class StoryView(generic.DetailView):
    """Class based view for viewing story"""
    template_name = '/read.html'
    model = Story
