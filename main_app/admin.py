from django.contrib import admin

from .models import Comment, Video

admin.site.register(Video)
admin.site.register(Comment)
