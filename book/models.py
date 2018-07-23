from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=120)
    imgLink = models.TextField()
    bookURL = models.URLField(default="http://avidreaders.ru/author/zhan-kristof-granzhe/")
    post = models.TextField()
    date = models.DateTimeField()
    like = models.IntegerField(default=0)
    authot = models.CharField(max_length=120)
    authorURL = models.URLField(default="https://ru.wikipedia.org/wiki/")
    authorData = models.TextField()
    authotImgLink = models.TextField()


    def __str__(self):
        return self.title
