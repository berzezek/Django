from django.shortcuts import render
from .models import News
from django.views.generic import ListView

# Create your views here.


def home(request):
    return render(request, 'h_work_15/index.html')

def uslugi(request):
    return render(request, 'h_work_15/uslugi.html')

def about(request):
    return render(request, 'h_work_15/about.html')

# class ShowNews(ListView):
#     model = News
#     template_name = 'h_work_15/news.html'
#     contex_object_name = 'news'
#     ordering = ['id']
#
#     def get_contex_data(self, **kwards):
#         ctx = super(ShowNewsView, self).get_contex_data(**kwards)
#
#         ctx['title'] = 'Главная страница сайта'
#         return ctx

def news(request):
    data = {
    'news': News.objects.all(),
    }

    return render(request, 'h_work_15/news.html', data)
