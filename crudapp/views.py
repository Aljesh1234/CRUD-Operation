from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import EmployeerForm
from .models import *
from . import views

# Create your views here.

def index(request):
    employee= Person.objects.all().count()
    context = {
        'employee':employee
    }
    return render(request,'index.html',context)
    


def employee(request):
    if request.method =='POST':
        data = request.POST
        first_name = data['first_name'] 
        last_name = data['last_name']
        email = data['email']

        obj = Person.objects.create(first_name = first_name,
                              last_name = last_name,
                              email= email)
        if obj: 
            return redirect('/employee')
        return HttpResponse ("Employees is not created")
    else:
         person = Person.objects.all()
         context = {
        'persons': person
    }
    return render(request,"employee.html",context)





def update(request,id):
    # print(request)
    # we're fetching the data through here
    person = Person.objects.get(id = id)    
    if request.method == 'POST':
        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.email = request.POST['email']
        person.save()

        return redirect('/employee')
    context ={
            'person' : person
    }
    return render(request,'update.html', context)


def delete(request,id):

    # print(request)
    # we're fetching the data through here
    person = Person.objects.get(id = id)    
    if request.method == 'POST':
        person.delete()
        return redirect('/employee')    
    context ={
            'person' : person
    }
    return render(request,'delete.html', context)




