from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import fiction_page_view, homepage_view, fiction_create_view, fiction_edit_view


app_name = "fiction_fans"
urlpatterns = [
    path("", homepage_view.HomePage.as_view(), name="homepage"),

    path("<int:fiction_id>/", fiction_page_view.fiction_view, name="fiction_view"),

    path("createfic/", fiction_create_view.create_fiction, name="fiction_create"),

    path("<int:fiction_id>/edit/", fiction_edit_view.edit_fiction, name="fiction_edit"),

    path("<int:fiction_pk>/<int:chapter_pk>/", fiction_page_view.ChapterView.as_view(), name="chapter_view"),

    path("createchap/", fiction_create_view.create_chapter, name="chapter_create"),

    path("<int:fiction_id>/<int:chapter_id>/edit/", fiction_edit_view.edit_chapter, name="chapter_edit"),

    path("imageUPload/", csrf_exempt(fiction_page_view.upload_image_view)),
]
