from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Media


def get_media(request: HttpRequest, media_id: int) -> HttpResponse:
    media = Media.objects.get(pk=media_id)
    context = {
        "title": media.title,
        "media": media,
    }
    return render(request, "minitube/media.html", context=context)


def gallery(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Gallery",
        "medias": Media.objects.all(),
    }
    return render(request, "minitube/gallery.html", context=context)


def home(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home",
        "medias": Media.objects.first()[3:],
    }
    return render(request, "minitube/home.html", context=context)
