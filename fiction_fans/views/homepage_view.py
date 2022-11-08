"""Create view for web homepage."""
from django.shortcuts import render
from ..models.fiction_model import FictionTitle

# Create your views here.

def homepage(request):
    """
    Create view for web homepage.
    Contain all fiction and display in homepage.
    """
    template_name = "homepage.html"
    fictions = FictionTitle.objects.all()
    context = {
        "fictions": fictions,
    }
    return render(request, template_name, context=context)
