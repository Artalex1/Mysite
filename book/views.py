from django.shortcuts import render, redirect
from book.models import Articles

def addlike(request, pk):
    path = request.path
    if 'addlikes' in path:
        response = redirect('/book/')
    else:
        response = redirect('/book/' + pk)
    if pk not in request.COOKIES or request.COOKIES.get(pk) == "delete_test":
        art = Articles.objects.get(id=pk)
        art.like += 1
        art.save()
        response.set_cookie(pk, "test")
        return response
    elif request.COOKIES.get(pk) == "test":
        art = Articles.objects.get(id=pk)
        art.like -= 1
        art.save()
        response.set_cookie(pk, "delete_test")
        return response
