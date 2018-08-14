from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=80)
    file_data = models.FileField()
    youtube = models.BooleanField(default=False)
    thumbnail = models.URLField()
