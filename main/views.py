from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from main.form import RegistrationForm
from django.shortcuts import get_object_or_404, render


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Users, Degrees, Courses, DegreeRequirements, CompletedClasses
from main.frms import AccountForm, RegistrationForm, StudentReadOnly, PlanForm
from main.planner import Planner

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
    degrees = DegreeRequirements.objects.all().order_by('course_id__course_id')
    return render(request,'main/browse.html',{'courses':courses, 'degrees':degrees})

def plan(request):
    myplan = [[]]
    if request.method == 'POST':
        mjr     = request.POST['mjr']
        start   = request.POST['start']
        rate    = request.POST['rate']
        
        taken   = []
        credits = 0
        deg_cred = Degrees.objects.get(id = mjr)
        reqs_cls    = DegreeRequirements.objects.filter(degree_id__id = mjr).order_by('-required','course_id__course_id')
        reqs    = [req.course_id for req in reqs_cls]
        for r in reqs: print r.course_id
        print (" \n\n")
        courses = Courses.objects.all()
        courses = [c for c in courses if c not in reqs]
        courses = reqs + courses
        
        if request.user.is_authenticated():
            taken   = CompletedClasses.objects.filter(studentID = request.user.id)
            t    = [cls.courseID for cls in taken]
            courses = [c for c in courses if c not in t]
            usr     = Users.objects.get(usr_acct=request.user.id)
            credits = usr.creditCnt
        

        plnr    = Planner(start, mjr, rate, reqs)
        myplan  = plnr.plan(courses, taken, start, rate, deg_cred.reqcredits)
        
    form = PlanForm()
    return render(request,'main/plan.html',{'form':form,'plan':myplan})

@login_required(login_url='login')
def account(request):
    classes_taken = CompletedClasses.objects.filter(studentID = request.user.id)
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
def addClass(request):
    classid =  request.POST['addclass']
    crse    =  Courses.objects.get(course_id = classid)
    usr     = Users.objects.get(usr_acct=request.user.id)
    taken   =  CompletedClasses(studentID = usr, courseID = crse)
    taken.save()
    return HttpResponseRedirect('account')
    
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

