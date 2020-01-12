"""tivix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import teachers, mystudents, student, star, profile, signin, \
    signout, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', include('api.students.urls')),
    path('api/teachers/', include('api.teachers.urls')),
    path('api/star/', include('api.star.urls')),
    path('teachers/', teachers, name='teachers'),
    path('mystudents/', mystudents, name='mystudents'),
    path('student/', student, name='nostudent'),
    path('student/<int:id>/', student, name='student'),
    path('star/', star, name='star'),
    path('profile/', profile, name='profile'),
    path('', signin, name='home'),
    path('logout/', signout, name='logout'),
    path('register/', register, name='register'),
    path('oauth/', include('social_django.urls', namespace='social')),
]

