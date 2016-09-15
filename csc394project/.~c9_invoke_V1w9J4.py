from django.db import models
from django.contrib.auth.models import User

#extend Django User model
class Users(User):
    creditCnt  = models.IntegerField()
    isEnrolled  = models.BooleanField()
    isFaculty   = models.BooleanField()

#Course Table
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
    dormant     = models.BooleanField()

#Degree (Degree ID, Degree Name)    
class Degrees(models.Model):
    name        = models.CharField(max_length=128, unique=True)
    credits     = models.IntegerField()
    

#Degree Requirements     
class DegreeRequirements(models.Model):
    degree_id   = models.ForeignKey(Degrees.id)
    course_id   = models.ForeignKey(Courses.course_id)
    required    = models.BooleanField()
    phase       = models.IntegerField()
    online      = models.BooleanField()
    
    
    
    