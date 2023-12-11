from django.shortcuts import render, redirect

from eva_app.form import WorkForm
from eva_app.models import Employee


# Create your views here.
def work1(request):
    return render(request,'intro.html')

def view(request):
    data = Employee.objects.all()
    return render(request,'view.html',{'data1':data})

def create(request):
    form=WorkForm()
    if request.method == 'POST':
        data=WorkForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request,'create.html',{'form':form})

def update(request,id):
    work=Employee.objects.get(id=id)
    form= WorkForm(instance=work)
    if request.method == 'POST':
        form=WorkForm(request.POST,instance=work)
        if form.is_valid():
            form.save()
            return redirect('view.html')
    return render(request,'update.html',{'form':form})


def delt(request,id):
    if request.method == "POST":
        data = Employee.objects.get(id=id)
        data.delete()
        return redirect('new1')


