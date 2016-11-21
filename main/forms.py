# from django import forms
# from models import Users, Degrees
# from django.contrib.auth.forms import UserCreationForm

# class AccountForm(forms.Form):
#     first   = forms.CharField(label="First name", required=True)
#     last    = forms.CharField(label="Last name", required=True)
#     usrname = forms.CharField(label="Username", required=True)
#     email   = forms.EmailField(label="Email", required=True)
#     mjr     = forms.ChoiceField(label="Major", choices=[(1,'BS CS'),(2,'BS IT'),(3,'MS CS'),(4,'MS IT')],required=True)
#     enrled  = forms.BooleanField(required=False, label="Enrolled")
#     fclty   = forms.BooleanField(required=False, label="Faculty")
    
#     def save(self, usr, commit=True):
#         user = usr
#         user.first_name  = self.cleaned_data['first']
#         user.last_name   = self.cleaned_data['last']
#         user.email  = self.cleaned_data['email']
#         user.degree = self.cleaned_data['mjr']
#         user.isEnrolled = self.cleaned_data['enrled']
#         user.isFaculty  = self.cleaned_data['fclty']
        
#         if commit:
#             user.save()
#         return user
 
# class StudentReadOnly(forms.Form):
#     first   = forms.CharField(label="First name", disabled=True, required=True)
#     last    = forms.CharField(label="Last name", disabled=True, required=True)
#     usrname = forms.CharField(label="Username", disabled=True, required=True)
#     email   = forms.EmailField(label="Email", disabled=True, required=True)
#     mjr     = forms.ChoiceField(label="Major", disabled=True, choices=[(1,'BS CS'),(2,'BS IT'),(3,'MS CS'),(4,'MS IT')],required=True)
#     enrled  = forms.BooleanField(required=False, disabled=True, label="Enrolled")
    
    
# class RegistrationForm(UserCreationForm):
#     first   = forms.CharField(label="First name",required=True)
#     last    = forms.CharField(label="Last name", required=True)
#     email   = forms.EmailField(label="Email", required=True)
#     mjr     = forms.ChoiceField(label="Major", choices=[(1,'BS CS'),(2,'BS IT'),(3,'MS CS'),(4,'MS IT')],required=True)
#     enrled  = forms.BooleanField(required=False, label="Enrolled")
#     fclty   = forms.BooleanField(required=False, label="Faculty")
    
        
#     def save(self,commit = True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first_name  = self.cleaned_data['first']
#         user.last_name   = self.cleaned_data['last']
#         user.email  = self.cleaned_data['email']
        
#         new_usr = Users(user)
#         new_usr.isEnrolled  = self.clean_data['enrled']
#         deg_name = self.clean_data['mjr']
#         deg = Degrees.objects.get(name=deg_name)
#         new_usr.degree_id = deg.id
#         new_usr.isEnrolled     = self.cleaned_data['enrled']
#       # new_usr.degree_id     = self.clean_data['mjr']
#         new_usr.isFaculty   = self.clean_data['fclty']
#         if commit:
#             new_usr.save()
#         return new_usr
        