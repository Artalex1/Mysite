from django.db import models

class Video(models.Model):
    Video_URL = models.TextField(default="https://youtube.com/embed/")
    Video_title = models.CharField(max_length=200, default="")
    Video_o = models.TextField(default="")
    Video_like = models.IntegerField(default=0)
    Video_time = models.DateTimeField()

    class Meta():
        db_table = "Video"

    def __str__(self):
        return self.Video_title

class Comment(models.Model):
    class Meta():
        db_table = "Comment"
    comment_text = models.TextField(verbose_name="Комментарий")
    comment_video = models.ForeignKey(Video, True)

    def __str__(self):
        return self.comment_text