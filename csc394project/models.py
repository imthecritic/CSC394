from django.db import models
from django.contrib.auth.models import User

#extend Django User model
class Users(User):
    isFaculty = models.BooleanField()

class Courses(models.Model):
    course_id   = models.CharField(max_length=6, unique=True)
    name        = models.CharField(max_length=128,unique=True)
    description = models.CharField(max_length=128)
    prereq      = models.CharField(max_length=128)
    credits     = models.IntegerField()
    fall        = models.BooleanField()
    winter      = models.BooleanField()
    spring      = models.BooleanField()
    summer      = models.BooleanField()
    
class Degrees(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
class DegreeRequirements(models.Model):
    degree_id   = models.ForeignKey(Degrees.id)
    course_id   = models.ForeignKey(Courses.course_id)
    required    = models.BooleanField()
    
    
    
    