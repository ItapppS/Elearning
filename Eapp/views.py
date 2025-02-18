from django.shortcuts import render

# Create your views here.

def demo(request):
    return render(request, 'demo.html')

def robotics(request): 
    return render(request, 'robotics.html')

def about(request): 
    return render(request, 'about.html')

def otto(request): 
    return render(request, 'otto.html')

def profile(request): 
    return render(request, 'profile.html')

def cart(request): 
    return render(request, 'cart.html')

def base(request): 
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')