"""Homepage view for web application."""
from ..models.fiction_model import FictionTitle
from django.utils import timezone
from django.views import generic

# Create your views here.


class HomePage(generic.ListView):
    """Homepage view for listing all fiction's title."""
    template_name = "fiction_fans/homepage.html"
    context_object_name = "fictions"

    def get_queryset(self):
        return FictionTitle.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
