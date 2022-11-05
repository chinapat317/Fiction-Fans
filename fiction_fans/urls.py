from django.urls import path
from . import views

urlpatterns = [
    path("fiction/<int:fiction_id>/<int:chapter_id>", ChapterView.as_view, name="chapter_view"),
]
