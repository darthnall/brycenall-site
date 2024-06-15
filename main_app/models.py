from django.core.files.storage import storages
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="comments"
    )
    video = models.ForeignKey(
        "Video", on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField(max_length=2048, default="")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.id} - {self.user}"


class Media(models.Model):
    title = models.CharField(max_length=256)
    desc = models.TextField(max_length=2048, default="")
    slug = models.SlugField(max_length=64, default="")
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    source = models.FileField(storage=storages["bucket"])
    date_uploaded = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(storage=storages["bucket"], blank=True, null=True)
    duration = models.DurationField()

    def __str__(self) -> str:
        return self.title

    def is_photo(self) -> bool:
        return bool(self.duration)

    @property
    def url(self) -> str:
        return self.source.url

    @property
    def display_as(self) -> str:
        return self.title.title()

    def convert(self, fmt: str) -> str:
        raise NotImplementedError
