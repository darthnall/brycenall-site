from django.contrib.postgres.fields import ArrayField
from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=256)
    tags = ArrayField(models.CharField(max_length=32), blank=True)

    def __str__(self) -> str:
        return self.name
