from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PhnUser  # Import the model
from django.contrib.auth.hashers import make_password

# Create your views here.

def demo(request):
    return render(request, 'demo.html')

def robotics(request): 
    return render(request, 'robotics.html')

def about(request): 
    return render(request, 'about.html')

def otto(request): 
    return render(request, 'otto.html')

def bionic_hand(request):
    return render(request, 'bionic_hand.html')

def humanoid_robot(request):
    return render(request, 'humanoid_robot.html')

def home_automation(request):
    return render(request, 'home_automation.html')

def solar_tracking(request):
    return render(request, 'solar_tracking.html')

def obstraction_avoiding_car(request):
    return render(request, 'obstraction_avoiding_car.html')

def profile(request): 
    return render(request, 'profile.html')

def cart(request): 
    return render(request, 'cart.html')

def base(request): 
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def bionic_hand(request):
    return render(request, 'bionic_hand.html')

def asterbot(request):
    return render(request, 'asterbot.html')


def register(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username = request.POST.get('username')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        age = request.POST.get('age')
        gender=request.POST.get('gender',)
        address=request.POST.get('address')
        mobile_no = request.POST.get('mobile_no')

        # ✅ Input Validation
        if not username or not gmail or not password or not age or not mobile_no:
            messages.error(request, "All fields are required.")
            return redirect('register')

        if PhnUser.objects.filter(gmail=gmail).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        # ✅ Hash the password before saving
        hashed_password = make_password(password)

        # ✅ Save user manually (instead of using ModelForm)
        user = PhnUser(username=username, gmail=gmail, password=hashed_password, age=age, mobile_no=mobile_no)
        user.save()

        messages.success(request, "Registration successful! Now log in.")
        return redirect('home')

    return render(request, 'register.html')



    

