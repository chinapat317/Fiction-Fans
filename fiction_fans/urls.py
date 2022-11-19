from django.urls import path
from .views import (homepage_view
                    , fiction_view
                    , fiction_create_view
                    , fiction_edit_view
                    , comment
                    , ChapterView)


app_name = "fiction_fans"
urlpatterns = [
    path("", homepage_view.HomePage.as_view(), name="homepage"),
    path("<int:fiction_id>/", fiction_view, name="fiction_view"),
    path("createfic/", fiction_create_view.create_fiction, name="fiction_create"),
    path("<int:fiction_id>/edit/", fiction_edit_view.edit_fiction, name="fiction_edit"),
    path("<int:fiction_pk>/<int:chapter_pk>/", ChapterView.as_view(), name="chapter_view"),
    path("createchap/", fiction_create_view.create_chapter, name="chapter_create"),
    path("<int:fiction_id>/<int:chapter_id>/edit/", fiction_edit_view.edit_chapter, name="chapter_edit"),
    path("<int:fiction_pk>/<int:chapter_pk>/comment/", comment, name="chapter_comment"),
]
