from django.shortcuts import render

def home_view(request):
    title = "Welcome to Django"
    
    return render(request, 'index.html', {'title': title})


def index_view(request):
    
    return render(request,  'base.html')