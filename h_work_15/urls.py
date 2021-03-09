from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uslugi', views.uslugi, name='uslugi'),
    path('about', views.about, name='about'),
    path('news', views.ShowNewsView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'),
    # path('news', views.news, name='news'),
]
