from datetime import datetime

from django.core.files.storage import storages
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    media = models.ForeignKey("Media", on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=256)

    date_uploaded = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(default=datetime.now)

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class MediaCategory(models.Model):
    class Meta:
        verbose_name_plural = "Media Categories"

    name = models.CharField(max_length=64)
    source = models.ImageField(null=True, blank=True, storage=storages["bucket"])

    def url(self) -> str:
        return self.source.url

    def __str__(self) -> str:
        return self.name


class Media(models.Model):
    name = models.CharField(max_length=256, unique=True)
    source = models.FileField(storage=storages["bucket"])
    desc = models.TextField(max_length=2048, default="")
    caption = models.CharField(max_length=256, default="")
    thumb = models.ImageField(null=True, blank=True, storage=storages["bucket"])
    category = models.ManyToManyField(
        "MediaCategory",
        related_name="categories",
        blank=True,
    )

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments = models.ManyToManyField(
        "Comment",
        related_name="comments",
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    def title(self) -> str:
        return self.name.title()

    def url(self) -> str:
        return self.source.url
