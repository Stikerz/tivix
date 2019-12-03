from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render


def teachers(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'teachers.html', context)
    else:
        raise Http404("Page cannot be found")

