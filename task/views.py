from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task

def task(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskForm()
    return render(request,'addtask.html',{'form':form})

# Create your views here.
def homepage(request):
    data = Task.objects.all()
    return render (request,'homepage.html',{'data':data})

def edittask(request,id):
    target = Task.objects.get(pk=id)
    form = TaskForm(instance=target)
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'addtask.html',{'form':form})




def deletetask(request,id):
    target = Task.objects.get(pk=id)
    target.delete()
    return redirect('homepage')
