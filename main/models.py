from django.db import models
from django.contrib.auth.models import User


#Course Table
class Courses(models.Model):
    id          = models.AutoField(primary_key=True)
    course_id   = models.CharField(max_length=6, unique=True)
    name        = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    prereq      = models.CharField(max_length=128)
    credits     = models.IntegerField()
    fall        = models.BooleanField()
    winter      = models.BooleanField()
    spring      = models.BooleanField()
    summer      = models.BooleanField()
    dormant     = models.BooleanField()
    cs_class    = models.BooleanField()
    is_class    = models.BooleanField()

#Degree (Degree ID, Degree Name)    
class Degrees(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=128, unique=True)
    reqcredits  = models.IntegerField()
    online      = models.BooleanField()

#Degree Requirements     
class DegreeRequirements(models.Model):
    degree_id   = models.ForeignKey(Degrees)
    course_id   = models.ForeignKey(Courses)
    #required    = models.BooleanField()
    phase       = models.IntegerField()
    
#extend Django User model
class Users(models.Model):
#    first       = models.CharField(max_length=128)
#    last        = models.CharField(max_length=128)
    usr_acct         = models.OneToOneField(User, on_delete=models.CASCADE)
    degree      = models.ForeignKey(Degrees, default=None)
    creditCnt   = models.IntegerField(default=0)
    isEnrolled  = models.BooleanField()
    isFaculty   = models.BooleanField()    
    
class CompletedClasses(models.Model):
    studentID   = models.ForeignKey(Users)
    courseID    = models.ForeignKey(Courses)
    from django.db import models
from django.contrib.auth.models import User


