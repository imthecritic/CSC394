
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from models import Users, Degrees
from frms import AccountForm, RegistrationForm
#INDEX PAGE
def index(request):
   # return HttpResponse('<html lang="en"py><head><meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1">  <!-- Latest compiled and minified CSS --> <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script> </head> <body> <h1>Course Planner</h1> <button>Plan</button> </body>')
    
    return render(request, 'main/index.html', {})
    
def loginPage(request):
    if request.method == 'POST':
        usr = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usr, password=pwd)
        
        if user is not None:
            login(request,user)
            print("success")
            return render(request, 'main/index.html', {})
        else:
            return HttpResponseRedirect('login')
    return render(request, 'main/login.html', {})

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('login')
    
def register(request):
    deg                 = Degrees.objects.all()
    if len(deg) == 0:
        d = Degrees(name='BS CS',reqcredits=120,online=True)
        d.save()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            print(user.id)
            a = User.objects.get(id=user.id)
            newusr = Users()
            newusr.usr_acct = a
            newusr.isEnrolled = request.POST['enrled']
            newusr.isFaculty = request.POST['fclty']
            deg = Degrees.objects.all()
            deg = deg[0]
            newusr.degree = deg
            newusr.save()
            return render(request,'main/login.html',{})
            
    else:
        form = RegistrationForm()
        
    return render(request,'main/register.html',{'form': form})


def browse(request):
    return render(request,'main/browse.html',{})

def plan(request):
    return render(request,'main/plan.html',{})

@login_required(login_url='login')
def account(request):
    classes_taken = []
    #user = Users.objects.get()
    
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save(request.user)
    else:
        usr = Users.objects.get(usr_acct=request.user.id)
        usrinfo = usr.usr_acct
        #if user is faculty add a list of students they can assume identity of. 
        form = AccountForm(initial={'first':usrinfo.first_name,'last':usrinfo.last_name,'email':usrinfo.email,'usrname':usrinfo.username,'fclty':usr.isFaculty,'enrled':usr.isEnrolled})
    return render(request,'main/account.html',{'form':form, 'classes_taken':classes_taken})

def about(request):
    pass
