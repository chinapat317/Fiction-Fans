from django.urls import path
from . import views 

app_name = "fiction_fans"
urlpatterns = [
    # path("fiction/<int:fiction_id>/<int:chapter_id>", chapter_view.ChapterView.as_view(), name="chapter_view"),
    path("home", views.HomePage.as_view(), name="homepage"),
    path("<int:fiction_id>/detail", views.fiction_view, name="fiction_page"),
    path("<int:title_pk>/<int:chapter_pk>/read", views.ChapterView.as_view(), name="chapter_page"),
]
