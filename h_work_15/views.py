from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def home(request):
    return render(request, 'h_work_15/index.html')

def uslugi(request):
    return render(request, 'h_work_15/uslugi.html')

def about(request):
    return render(request, 'h_work_15/about.html')

class ShowNewsView(ListView):
    model = News
    template_name = 'h_work_15/news.html'
    context_object_name = 'news'
    ordering = ['-date']


    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Новости'
        return ctx

class NewsDetailView(DetailView):
    model = News
    template_name = 'h_work_15/news_detail.html'
    # context_object_name = 'post'
    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    # template_name='h_work_15/news_form.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
