from django.urls import path
from .views import fiction_view, homepage_view

urlpatterns = [
    # path("fiction/<int:fiction_id>/<int:chapter_id>", chapter_view.ChapterView.as_view(), name="chapter_view"),
    path("", homepage_view.homepage, name="homepage"),
    path("novel/<int:fiction_id>/", fiction_view.fiction_view, name="fiction_view"),
    path("novel/<int:fiction_id>/<int:chapter_id>", fiction_view.chapter_view, name="chapter_view"),
]
