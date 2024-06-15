from django.contrib import admin

from .models import Comment, Media

admin.site.register(Comment)
admin.site.register(Media)
