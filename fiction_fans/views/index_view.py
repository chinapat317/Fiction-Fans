"""All fiction by rate and submitted time for web homepage."""
from ..models.fiction_model import FictionTitle
from django.utils import timezone
from django.views import generic

# Create your views here.


class HotPage(generic.ListView):
    """Hot page view for listing all fiction sorted by rate."""
    template_name = "fiction_fans/hot_page.html"
    context_object_name = "hot_fictions"

    def get_queryset(self):
        all_fiction = FictionTitle.objects.all()
        sorted_by_rate = sorted(
            all_fiction,
            key= lambda r: r.average_rate_all_chapters()
        ) 
        return sorted_by_rate


class RecentlyPage(generic.ListView):
    """Recently view for listing all fiction sorted by submitted date."""
    template_name = "fiction_fans/recently_page.html"
    context_object_name = "recently_fictions"

    def get_queryset(self):
        return FictionTitle.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')
