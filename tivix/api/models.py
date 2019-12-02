from django.db import models
from django.contrib.auth.models import AbstractUser

# TODO: Slugify ?


class Student(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    age = models.DateField(null=False)
    year = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(AbstractUser):
    students = models.ManyToManyField(Student, blank=True)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StarStudent(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    star = models.BooleanField(null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['teacher', 'student'],
                                    name='unique_star')
        ]

