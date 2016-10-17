
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from main.form import RegistrationForm
from django.shortcuts import get_object_or_404, render


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Users, Degrees, Courses
from main.frms import AccountForm, RegistrationForm, StudentReadOnly
#INDEX PAGE
def index(request):

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
            # a = User.objects.get(id=user.id)
            # newusr = Users()
            # newusr.usr_acct = a
            # newusr.isEnrolled = request.POST['enrled']
            # newusr.isFaculty = request.POST['fclt'] if request.POST['fclty'] != None else False
            # deg = Degrees.objects.all()
            # deg = deg[0]
            # newusr.degree = deg
            # newusr.save()
            return render(request,'main/login.html',{})
            
    else:
        form = RegistrationForm()
        
    return render(request,'main/register.html',{'form': form})


def coursecatalog(request):
    return render(request, 'main/coursecatalog.html', {})

def browse(request):
    courses = Courses.objects.all()
    return render(request,'main/browse.html',{'courses':courses})

def plan(request):
    return render(request,'main/plan.html',{})

@login_required(login_url='login')
def account(request):
    classes_taken = []
    permission = False
    
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save(request.user)
    else:
        usr = Users.objects.get(usr_acct=request.user.id)
        usrinfo = usr.usr_acct
        permission = usr.isFaculty
        #if user is faculty add a list of students they can assume identity of. 
        form = AccountForm(initial={'first':usrinfo.first_name,'last':usrinfo.last_name,'email':usrinfo.email,'usrname':usrinfo.username,'fclty':usr.isFaculty,'enrled':usr.isEnrolled})
    studentlst = Users.objects.filter(isFaculty=False)
    return render(request,'main/account.html',{'form':form, 'classes_taken':classes_taken, 'studentlst':studentlst,'permission':permission})

@login_required(login_url='login')
def view_student(request, username):
    uname = username
    classes_taken = []
    stu = User.objects.get(username=uname)
    stu2 = Users.objects.get(usr_acct = stu)
    usrinfo = stu
    #if user is faculty add a list of students they can assume identity of. 
    form = StudentReadOnly(initial={'first':usrinfo.first_name,'last':usrinfo.last_name,'email':usrinfo.email,'usrname':usrinfo.username,'enrled':stu2.isEnrolled})
    return render(request,'main/view_student.html',{'form':form, 'classes_taken':classes_taken})
    
def about(request):
    pass

