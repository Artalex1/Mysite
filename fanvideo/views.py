from django.shortcuts import render, redirect
from fanvideo.models import Video, Comment
from django.http import HttpResponse
from django.template.context_processors import csrf
from . import forms
from django.contrib import auth

#def Hello(request):
 #   return HttpResponse('<H1>Hello fucking world!!!</H1>')

#def Hello(request):
#    return render(request, 'videop.html')

def hello(request, Video_id):
    return HttpResponse('<h1>Hello world!!</h1>')

def onevideo(request, Video_id):
    comment_form = forms.CommentForm
    args = {}
    args.update(csrf(request))
    args['video'] = Video.objects.get(id=Video_id)
    args['comment'] = Comment.objects.filter(comment_video_id=Video_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'onevideo.html', args)

def addcomment1(request, Video_id):
    if request.POST:
        forma = forms.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            comment.comment_video = Video.objects.get(id=Video_id)
            forma.save()
    return redirect('/FanVideo/onevideo/' + Video_id)

def addcomment(request, Video_id):
    if request.POST and ('pause' not in request.session):
        forma = forms.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            comment.comment_video = Video.objects.get(id=Video_id)
            forma.save()
            # выдержка в 60 c
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/FanVideo/onevideo/' + Video_id)

def addlikes1(request, Video_id):
    video = Video.objects.get(id=Video_id)
    video.Video_like += 1
    video.save()
    path = request.path
    if 'Vadd' in path:
        return redirect('/FanVideo/')
    return redirect('/FanVideo/onevideo/' + Video_id)

def addlikes(request, Video_id):
    path = request.path
    if Video_id not in request.COOKIES:
        video = Video.objects.get(id=Video_id)
        video.Video_like += 1
        video.save()
        if 'Vadd' in path:
            response = redirect('/FanVideo/')
        else:
            response = redirect('/FanVideo/onevideo/' + Video_id)
        response.set_cookie(Video_id, "test")
        return response
    if 'Vadd' in path:
        return redirect('/FanVideo/')
    return redirect('/FanVideo/onevideo/' + Video_id)

def dislikes(request, Video_id):
    video = Video.objects.get(id=Video_id)
    video.Video_like -= 1
    video.save()
    path = request.path
    if 'Vd' in path:
        return redirect('/FanVideo/')
    return redirect('/FanVideo/onevideo/' + Video_id)

def WorkBD(request):
    class content(Video):
        comments = ""
    content_list = []
    for i in Video.objects.all():
        j = content()
        j.Video_URL = i.Video_URL
        j.Video_title = i.Video_title
        j.Video_o = i.Video_o
        j.Video_like = i.Video_like
        j.Video_time = i.Video_time
        j.id = i.id
        j.comments = Comment.objects.filter(comment_video_id=i.id)
        content_list.append(j)
    return render(request, 'videop.html', {'Video': content_list, "username": auth.get_user(request).username})
