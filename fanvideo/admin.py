from django.contrib import admin
from fanvideo.models import Video, Comment


class VideoInline(admin.StackedInline):
    model = Comment
    extra = 2

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

admin.site.register(Video, VideoAdmin)