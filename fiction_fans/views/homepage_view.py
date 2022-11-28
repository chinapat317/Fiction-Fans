"""Create view for web homepage."""
from ..models.fiction_model import FictionTitle
from django.views import generic
from django.utils import timezone

# Create your views here.


class HomePage(generic.ListView):
    """Create view for homepage list all fiction's title."""
    template_name = "fiction_fans/homepage.html"
    context_object_name = "fictions"

    def get_queryset(self):
        return FictionTitle.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
