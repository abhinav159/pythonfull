from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'usertemplates/homepage.html')
    
def village(request):
    return render(request,'usertemplates/village.html')

def calculator(request):
    return render(request,'usertemplates/calculator.html')

def login(request):
    return render(request,'usertemplates/login.html')

def dom(request):
    return render(request,'usertemplates/dom.html')
def jquery(request):
    return render(request,'usertemplates/jquery.html')