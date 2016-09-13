from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    course_id = models.CharField(max_length=6, unique=True)
    name = models.CharFi
    