from typing import Optional, Union

from django import forms
from django.core.files.storage import storages
from django.db import models


class NewsletterSignupForm(forms.Form):
    name = forms.CharField(initial="Your name")
    email = forms.EmailField(initial="Your email")
    opted_in = forms.CheckboxInput()


class Video(models.Model):
    title = models.CharField(max_length=256)
    desc = models.TextField(max_length=2048, default="")
    source = models.FileField(storage=storages["video"])

    def __str__(self) -> str:
        return self.title

    @property
    def url(self) -> str:
        return self.source.url

    @property
    def display_as(self) -> str:
        return self.title.title()
