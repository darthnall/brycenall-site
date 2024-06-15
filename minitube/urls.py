from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:media_id>/", views.get_media, name="get media"),
    path("gallery/", views.gallery, name="gallery"),
]
