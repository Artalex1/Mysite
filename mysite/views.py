from django.shortcuts import render


def firstpage(request):
    return render(request, 'firstpage.html')


def about(request):
    return render(request, 'about.html')


def info(request):
    return render(request, 'info.html')


def game(request):
    return render(request, 'game.html')

