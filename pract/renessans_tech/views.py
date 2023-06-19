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

def laptops(request):
    return render(request, 'renessans_tech/laptops.html')

def byt_techn(request):
    return render(request, 'renessans_tech/byt_techn.html')

def computers(request):
    return render(request, 'renessans_tech/computers.html')

def tablets(request):
    return render(request, 'renessans_tech/laptops.html')

def smart_speakers(request):
    return render(request, 'renessans_tech/smart_speakers.html')

def basket(request):
    return render(request, 'renessans_tech/basket.html')