from django.shortcuts import render
from .models import Menu

def home(request):
    featured_menu = Menu.objects.all()[:6]
    return render(request, 'index.html', {'featured_menu': featured_menu})

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def menu_list(request):
    menu_list = Menu.objects.all()
    context = {'menu_list': menu_list}
    return render(request, 'menu.html', context)
