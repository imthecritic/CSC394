from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse

#INDEX PAGE
def index(request):
   # return HttpResponse('<html lang="en"><head><meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1">  <!-- Latest compiled and minified CSS --> <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script> </head> <body> <h1>Course Planner</h1> <button>Plan</button> </body>')
    return HttpResponse('We are winning')
    
def head(request):
    return HttpResponseRedirect('main/')
