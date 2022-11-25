from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from .forms import todoform
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class tlistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs= {'pk': self.object.id})

class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvfront')



def add(request):
    task=Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        variable=Task(name=name,priority=priority,date=date)
        variable.save()
    return render(request,'home.html',{'task':task})

def detail(request):
    task=Task.objects.all()
    return render(request, 'detail.html',{'task1':task})

def delete(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
        task=Task.objects.get(id=id)
        f1=todoform(request.POST or None, instance=task)
        if f1.is_valid():
            f1.save()
            return redirect('/')
        return render(request,'edit.html',{'task':task,'f1':f1 })