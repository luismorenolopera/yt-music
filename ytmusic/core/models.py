from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=60)
    file_data = models.FileField()
