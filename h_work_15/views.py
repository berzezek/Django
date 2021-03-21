from django.shortcuts import render
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name='h_work_15/news_form.html'
    fields = ['title', 'slug', 'long_link']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'h_work_15/news_form.html'

    fields = ['title', 'slug', 'long_link']


    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx


    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True

        return False


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'h_work_15/news_delete.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True

        return False
