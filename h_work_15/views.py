from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'h_work_15/index.html')

def uslugi(request):
    return render(request, 'h_work_15/uslugi.html')

def about(request):
    return render(request, 'h_work_15/about.html')
