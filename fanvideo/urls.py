from django.urls import include, re_path
from fanvideo.views import addlikes, dislikes, hello, onevideo, WorkBD, addcomment

urlpatterns = [
    re_path(r'^$', WorkBD),
    re_path(r'addlikes/(?P<Video_id>\d+)$', addlikes),
    re_path(r'dislikes/(?P<Video_id>\d+)$', dislikes),
    re_path(r'Vaddlikes/(?P<Video_id>\d+)$', addlikes),
    re_path(r'Vdislikes/(?P<Video_id>\d+)$', dislikes),
    re_path(r'^onevideo/(?P<Video_id>\d+)$', onevideo),
    re_path(r'^addcomment/(?P<Video_id>\d+)$', addcomment),

]