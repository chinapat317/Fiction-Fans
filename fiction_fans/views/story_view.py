from django.views import generic

# importing module
import ..models.story import Story


class StoryView(generic.DetailView):
    """Class based view for viewing story"""
    template_name = '/read.html'
    model = Story
