from django.contrib import admin
from api.models import Teacher, Student, StarStudent
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StarStudent)

