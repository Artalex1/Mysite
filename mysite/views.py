from django.shortcuts import render

def firstpage(request):
    return render(request, 'firstpage.html')