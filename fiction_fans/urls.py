from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from fiction_fans import views

app_name = "fiction_fans"
urlpatterns = [
    path("", views.HomePage.as_view(), name="homepage"),
    path("<int:fiction_id>/", views.fiction_view, name="fiction_view"),
    path("createfic/", views.create_fiction, name="fiction_create"),
    path("<int:fiction_id>/edit/", views.edit_fiction, name="fiction_edit"),
    path("<int:fiction_id>/del/", views.delete_fiction, name="fiction_del"),
    path("<int:fiction_pk>/<int:chapter_pk>/", views.ChapterView.as_view(), name="chapter_view"),
    path("<int:fiction_pk>/createchap/", views.create_chapter, name="chapter_create"),
    path("<int:fiction_id>/<int:chapter_id>/edit/", views.edit_chapter, name="chapter_edit"),
    path("<int:fiction_id>/<int:chapter_id>/del/", views.delete_chapter, name="chapter_del"),
    path("imageUPload/", csrf_exempt(views.upload_image_view)),
    path("<int:fiction_pk>/<int:chapter_pk>/comment/", views.comment, name="chapter_comment"),
    path("user/", views.Profile.as_view(), name="profile"),
    path("<int:fiction_pk>/<int:chapter_pk>/rate/", views.rate, name="rate_chapter"),
]
