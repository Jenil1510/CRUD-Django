from django.shortcuts import redirect, render
from .models import Student
# from django.db import models


# Create your views here.
def home(request):
    std=Student.objects.all()
    
    
    return render(request,"home.html", {'std':std})

def std_add(request):
    if request.method=='POST':
        print('Added')
        
        #retrive data 
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_phone=request.POST.get("std_phone")
        
        #create an object for model class
        
        s=Student()
        s.roll=std_roll
        s.name=std_name
        s.email=std_email
        s.phone=std_phone
        
        s.save()
        
        return redirect("/home")
    return render(request,"add_std.html")

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    
    return redirect("/home")

def update_std(request,roll):
    std=Student.objects.get(pk=roll)
        
    return render(request,"update_std.html",{'std':std})

def do_update_std(request,roll):
    std_roll=request.POST.get("std_roll")
    std_name=request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_phone=request.POST.get("std_phone")
    
    std=Student.objects.get(pk=roll)

    std.roll=std_roll
    std.name=std_name
    std.email=std_email
    std.phone=std_phone
    
    std.save()

    return redirect("/home")