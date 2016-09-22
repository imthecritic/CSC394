from django import forms
from models import Users
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    stu_id  = forms.CharField(label="Student ID", required=True)
    email   = forms.EmailField(label="Email", required=True)
    first   = forms.CharField(label="First name",required=True)
    last    = forms.CharField(label="Last name", required=True)
    mjr     = forms.ChoiceField(label="Major", choices=[(1,'BS CS'),(2,'BS IT'),(3,'MS CS'),(4,'MS IT')],required=True)
    enrled  = forms.BooleanField(label="Enrolled")
    fclty   = forms.BooleanField(label="Faculty")
    
        
    def save(self,commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first  = self.cleaned_data['first']
        user.last   = self.cleaned_data['last']
        user.email  = self.cleaned_data['email']
        user.degree = self.cleaned_data['mjr']
        
        user.isEnrolled = self.cleaned_data['enrled']
        user.isFaculty  = self.cleaned_data['fclty']
        
        
        if commit:
            user.save()
            
        return user
        