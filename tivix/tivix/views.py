from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
import json
from api.models import Teacher
from django.contrib.auth.hashers import check_password

from social_django.models import UserSocialAuth


def teachers(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, "teachers.html", context)
    else:
        raise Http404("Page cannot be found")


def mystudents(request):
    if request.user.is_authenticated:
        context = {"id": request.user.id}
        return render(request, "mystudents.html", context)
    else:
        raise Http404("Page cannot be found")


def student(request, id=None):
    if request.user.is_authenticated:
        context = {"id": id}
        return render(request, "student.html", context)
    else:
        raise Http404("Page cannot be found")


def profile(request):
    user = request.user
    if user.is_authenticated:
        try:
            github_login = user.social_auth.get(provider="github")
        except UserSocialAuth.DoesNotExist:
            github_login = None
        can_disconnect = user.social_auth.count() >= 1 or (
            user.has_email() and user.has_usable_password()
        )
        context = {
            "id": request.user.id,
            "github_login": github_login,
            "can_disconnect": can_disconnect,
        }
        return render(request, "profile.html", context)
    else:
        raise Http404("Page cannot be found")


def star(request):
    if request.user.is_authenticated:
        context = {"id": request.user.id}
        return render(request, "star.html", context)
    else:
        raise Http404("Page cannot be found")


def signin(request):
    """ Basic Authentication"""  # TODO: CHANGE!!!!
    if request.user.is_authenticated:
        return redirect("/mystudents/")
    else:
        if request.method == "POST":
            try:
                credentials = json.loads(request.body)
                password = credentials["password"]
                username = credentials["username"]
                user = Teacher.objects.get(username=username)
                crypted_password = user.password
                if check_password(password, crypted_password):
                    login(
                        request,
                        user,
                        backend="django.contrib.auth.backends.ModelBackend",
                    )
                    return redirect("/mystudents/")
            except Exception as e:
                pass
            raise Http404("Page cannot be found")
        context = {}
        return render(request, "login.html", context)


def signout(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.user.is_authenticated:
        return redirect("/mystudents/")
    else:
        context = {}
        return render(request, "register.html", context)
