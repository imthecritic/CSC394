# from django import forms
# from main.models import Users
# from django.contrib.auth.forms import UserCreationForm

# class RegistrationForm(UserCreationForm):
#     stu_id  = forms.CharField(label="Student ID", required=True)
#     email   = forms.EmailField(label="Email", required=True)
#     first   = forms.CharField(label="First Name",required=True)
#     last    = forms.CharField(label="Last Name", required=True)
#     mjr     = forms.ChoiceField(label="Major", choices=[(1,'BS CS'),(2,'BS IT'),(3,'MS CS'),(4,'MS IT')],required=True)
#     enrled  = forms.BooleanField(label="Enrolled")
#     fclty   = forms.BooleanField(label="Faculty")
    
        
#     def save(self,commit = True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first  = self.cleaned_data['First name']
#         user.last   = self.cleaned_data['Last name']
#         user.email  = self.cleaned_data['Email']
#         user.mjr    = self.cleaned_data['Major']
        
#         user.enrled = self.cleaned_data['Enrolled']
#         user.fclty  = self.cleaned_data['Faculty']
        
        
#         if commit:
#             user.save()
            
#         return user
        
    
    