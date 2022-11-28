"""Profile view for web application."""
from ..models.fiction_model import FictionTitle
from django.views import generic

# Create your views here.


class Profile(generic.ListView):
    """Profile view for listing all submitted fiction by that user."""
    template_name = "fiction_fans/profile_page.html"
    context_object_name = "fictions"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return FictionTitle.objects.filter(user=self.request.user)
