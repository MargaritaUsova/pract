from django.shortcuts import render
from .models import Task
from .forms import TaskForm
def index(request):
    tasks = Task.objects.all()
    return render(request, 'renessans_tech/index.html', {'title' : 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'renessans_tech/about.html')

def create(request):
    form = TaskForm()
    context = {
        'form' : form
    }
    return render(request, 'renessans_tech/create.html', context)

def phones(request):
    return render(request, 'renessans_tech/phones.html')