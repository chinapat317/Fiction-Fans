"""Create view for web homepage."""
from ..models.fiction_model import FictionTitle
from django.views import generic
from django.utils import timezone

# Create your views here.

class HotIndex(generic.ListView):
    """Create view for index list all fiction's title sorted by rate."""
    template_name = "fiction_fans/indexpage_hot.html"
    context_object_name = "hot_fictions"

    def get_queryset(self):
        return FictionTitle.objects.all()


class RecentlyIndex(generic.ListView):
    """Create view for index list all fiction's title sorted by published date."""
    template_name = "fiction_fans/indexpage_recently.html"
    context_object_name = "recently_fictions"

    def get_queryset(self):
        return FictionTitle.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
