from django.urls import re_path
from django.views.generic import ListView, DetailView
from book.models import Articles
from book.views import addlike

urlpatterns = [
    re_path(r'^$',
            ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
                             template_name="book/Book.html")),
    re_path(r'^(?P<pk>\d+)$',
            DetailView.as_view(model=Articles, template_name="book/Onebook.html")),

    re_path(r'addlike/(?P<pk>\d+)$', addlike),
    re_path(r'addlikes/(?P<pk>\d+)$', addlike),
]

