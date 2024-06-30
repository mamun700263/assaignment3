from django.shortcuts import render,redirect
from .forms import CategoryForm
# Create your views here.


def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print('hello')
        if form.is_valid():
            form.save()
            form = CategoryForm()
            # return redirect('homepage')
    else:
        form = CategoryForm()
    return render(request,'category.html',{'form':form})