from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from form import RegistrationForm

#INDEX PAGE
def index(request):
   # return HttpResponse('<html lang="en"><head><meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1">  <!-- Latest compiled and minified CSS --> <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script> </head> <body> <h1>Course Planner</h1> <button>Plan</button> </body>')
    return render(request, 'main/index.html', {})
    
def login(request):
    return render(request, 'main/login.html', {})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponse('Registered')
            
    else:
        form = RegistrationForm()
        
    return render(request,'main/register.html',{'form': form})


def coursecatalog(request):
    pass

def plan(request):
    pass

def settings(request):
    pass

def about(request):
    pass
