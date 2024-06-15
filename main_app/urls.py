from django.urls import path

from . import views

urlpatterns = [
    path("<int:video_id>/watch", views.get_video_stream, name="get video stream"),
    path(
        "<int:video_id>/download", views.get_video_downloads, name="get video downloads"
    ),
    path("<int:video_id>/update", views.update_video, name="update video"),
]
