"""Create the fiction and add mutiple chapter to fiction."""
from django.db import models
from django.conf import settings
from django_editorjs import EditorJsField
from django.utils import timezone

# Create your models here.
    

class FictionTitle(models.Model):
    """Create fiction that contain fiction's title and created date/time."""
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="Anonymous")
    status = models.CharField(max_length=255, default="ongoing")
    description = models.CharField(max_length=255, default=" ")
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
                        "additionalRequestHeaders": [{"Counter-Type": 'multipart/form-data'}]
                    }
                }
            }
        }
    )
    fiction_title = models.ForeignKey(FictionTitle, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.fiction_title}: {self.title}"
    
    def average_rate(self):
        """Return average rate of chapter."""
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
        return all_point/count
        
