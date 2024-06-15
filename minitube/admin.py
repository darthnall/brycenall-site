from django.contrib import admin

from .models import Comment, Media, MediaCategory

admin.site.register(Comment)
admin.site.register(Media)
admin.site.register(MediaCategory)
