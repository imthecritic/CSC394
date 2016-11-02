from django import forms
from main.models import Users, Degrees
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlanForm(forms.Form):
    mjr     = forms.ChoiceField(label="Major", choices=[(3,'MS CS: Software and Systems Development'),(4,'MS IS: Business Analysis/Systems Analysis'), (5,'MS IS: Standard')],required=True)
    start   = forms.ChoiceField(label="Start", choices=[(1,'Fall'),(2,'Winter'),(3,'Spring'),(4,'Summer')],required=True)
    rate    = forms.ChoiceField(label="Rate", choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],required=True)

    
class AccountForm(forms.Form):
    first   = forms.CharField(label="First name", required=True)
    last    = forms.CharField(label="Last name", required=True)
    usrname = forms.CharField(label="Username", required=True)
    email   = forms.EmailField(label="Email", required=True)
    mjr     = forms.ChoiceField(label="Major", choices=[(3,'MS CS: Software and Systems Development'),(4,'MS IS: Business Analysis/Systems Analysis'), (5,'MS IS: Standard')],required=True)
    enrled  = forms.BooleanField(required=False, label="Enrolled")
    fclty   = forms.BooleanField(required=False, label="Faculty")
    
    def save(self, usr, commit=True):
        user = usr
        user.first_name  = self.cleaned_data['first']
        user.last_name   = self.cleaned_data['last']
        user.email  = self.cleaned_data['email']
        user.degree = self.cleaned_data['mjr']
        user.isEnrolled = self.cleaned_data['enrled']
        user.isFaculty  = self.cleaned_data['fclty']
        
        if commit:
            user.save()
        return user
        
class StudentReadOnly(forms.Form):
    first   = forms.CharField(label="First name", disabled=True, required=True)
    last    = forms.CharField(label="Last name", disabled=True, required=True)
    usrname = forms.CharField(label="Username", disabled=True, required=True)
    email   = forms.EmailField(label="Email", disabled=True, required=True)
    mjr     = forms.ChoiceField(label="Major", choices=[(3,'MS CS: Software and Systems Development'),(4,'MS IS: Business Analysis/Systems Analysis'), (5,'MS IS: Standard')],required=True)
    enrled  = forms.BooleanField(required=False, disabled=True,  label="Enrolled")
    
class RegistrationForm(UserCreationForm):
    first   = forms.CharField(label="First name",required=True)
    last    = forms.CharField(label="Last name", required=True)
    email   = forms.EmailField(label="Email", required=True)
    mjr     = forms.ChoiceField(label="Major", choices=[(3,'MS CS: Software and Systems Development'),(4,'MS IS: Business Analysis/Systems Analysis'), (5,'MS IS: Standard')],required=True)
    enrled  = forms.BooleanField(required=False, label="Enrolled")
    fclty   = forms.BooleanField(required=False,initial=False, label="Faculty")
    
    def save(self,commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name  = self.cleaned_data['first']
        user.last_name   = self.cleaned_data['last']
        user.email  = self.cleaned_data['email']
        #user.save()
        

        if commit:
            user.save()
            a = User.objects.get(id=user.id)
            newusr = Users()
            newusr.usr_acct = a
            newusr.isEnrolled =self.cleaned_data['enrled']
            newusr.isFaculty = self.cleaned_data['fclty']
            deg = Degrees.objects.all()
            deg = deg[0]
            newusr.degree = deg
            newusr.save()
        return user