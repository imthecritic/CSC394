from django import forms
from models import Users
from django.contrib.auth.forms import UserCreationForm

class AccountForm(forms.Form):
    first   = forms.CharField(label="First name",required=True)
    last    = forms.CharField(label="Last name", required=True)
    usrname = forms.CharField(label="Username", required=True)
    email   = forms.EmailField(label="Email", required=True)
    mjr     = forms.ChoiceField(label="Major", choices=[(1,'BS CS'),(2,'BS IT'),(3,'MS CS'),(4,'MS IT')],required=True)
    enrled  = forms.BooleanField(initial=True, label="Enrolled")
    fclty   = forms.BooleanField(initial=True, label="Faculty")
    
class RegistrationForm(UserCreationForm):
    first   = forms.CharField(label="First name",required=True)
    last    = forms.CharField(label="Last name", required=True)
    email   = forms.EmailField(label="Email", required=True)
    mjr     = forms.ChoiceField(label="Major", choices=[(1,'BS CS'),(2,'BS IT'),(3,'MS CS'),(4,'MS IT')],required=True)
    enrled  = forms.BooleanField(initial=True, label="Enrolled")
    fclty   = forms.BooleanField(initial=True, label="Faculty")
    
        
    def save(self,commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name  = self.cleaned_data['first']
        user.last_name   = self.cleaned_data['last']
        user.email  = self.cleaned_data['email']
        user.degree = self.cleaned_data['mjr']
        
        user.isEnrolled = self.cleaned_data['enrled']
        user.isFaculty  = self.cleaned_data['fclty']
        
        
        if commit:
            user.save()
            
        return user
        