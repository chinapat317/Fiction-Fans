"""Create view for web homepage."""
from ..models.fiction_model import FictionTitle
from django.views import generic

# Create your views here.


class HomePage(generic.ListView):
    """Create view for homepage list all fiction's title."""
    template_name = "fiction_fans/homepage.html"
    context_object_name = "fictions"

    def get_queryset(self):
        return FictionTitle.objects.all()
