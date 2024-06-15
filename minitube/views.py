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
