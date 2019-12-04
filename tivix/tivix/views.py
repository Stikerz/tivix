from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render


def teachers(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'teachers.html', context)
    else:
        raise Http404("Page cannot be found")


def mystudents(request):
    if request.user.is_authenticated:
        context = {"id": request.user.id}
        return render(request, 'mystudents.html', context)
    else:
        raise Http404("Page cannot be found")


def student(request, id=None):
    if request.user.is_authenticated:
        context = {"id": id}
        return render(request, 'student.html', context)
    else:
        raise Http404("Page cannot be found")


def star(request):
    if request.user.is_authenticated:
        context = {"id": request.user.id}
        return render(request, 'star.html', context)
    else:
        raise Http404("Page cannot be found")

