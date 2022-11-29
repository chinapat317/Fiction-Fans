"""Model for fiction and add mutiple chapters to fictions."""
from django.db import models
from django.conf import settings
from django.utils import timezone
from django_editorjs import EditorJsField

# Create your models here.


STATUS_CHOICES = [
    ("Oneshot", "Oneshot"),
    ("Ongoing", "Ongoing"),
    ("Finish", "Finish"),
    ("Draft", "Draft"),
    ("Drop", "Drop"),
]


class FictionTitle(models.Model):
    """
    Create a fiction that contain:
    fiction's title,
    original author of the fiction,
    status of the fiction - (Oneshot, Ongoing, Finish, Drop),
    description of the fiction,
    date of submit the fiction.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    cover_url = models.CharField(
        max_length=255,
        default="https://firebasestorage.googleapis.com/v0/b/fiction-fans.appspot.com/o/no-cover.png?alt=media&token=007d2b16-2e97-409b-b5ed-c3729fa5dc3a"
    )
    author = models.CharField(max_length=255, default="Anonymous")
    translator = models.CharField(max_length=255, default="Anonymous")
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default="Ongoing"
    )
    description = models.CharField(max_length=255, default="")
    pub_date = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self) -> str:
        return self.title


class FictionChapter(models.Model):
    """
    Create a chapter for fiction that contain chapter's title
    and chapter's content.
    Connect each chapter to a single fiction by using ForeignKey.
    """
    title = models.CharField(max_length=255)
    content = EditorJsField(
        editorjs_config={
            "tools": {
                "Image": {
                    "config": {
                        "endpoints": {
                            "byFile": "/fiction/imageUPload/",
                            "byUrl": "/fiction/imageUPload/",
                        },
                        "additionalRequestHeaders": [
                            {"Counter-Type": 'multipart/form-data'}
                        ]
                    }
                }
            }
        }
    )
    fiction_title = models.ForeignKey(FictionTitle, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.fiction_title}: {self.title}"
    
    def average_rate(self):
        """Return average rated of the chapter."""
        chapter_rate = self.ratemodel_set.all()
        file = open("log.txt", "w")
        file.write("id = {}".format(self))
        file.close()
        all_point = 0
        count = 0
        for rate in chapter_rate:
            all_point += rate.point
            count += 1
        if count == 0 :
            return 0
        return all_point / count

