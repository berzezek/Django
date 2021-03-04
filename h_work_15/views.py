from django.shortcuts import render
from .models import News

# Create your views here.
def home(request):
    data = {
    'news': News.objects.all(),
    'title': 'Главная страница!'
    }
    return render(request, 'h_work_15/index.html', data)

def uslugi(request):
    return render(request, 'h_work_15/uslugi.html')

def about(request):
    return render(request, 'h_work_15/about.html')
