from django.urls import path

from . import views

urlpatterns = [
    path("<int:media_id>/", views.get_media, name="get media"),
]
