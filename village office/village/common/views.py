from django.shortcuts import render

# Create your views here.
def commonhome(request):
    return render(request,'commonhome.html')