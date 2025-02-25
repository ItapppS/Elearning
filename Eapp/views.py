from django.shortcuts import render, redirect

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




from .forms import PhnUserForm

def register(request):
    if request.method == "POST":
        form = PhnUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page after registration
    else:
        form = PhnUserForm()
    
    return render(request, 'register.html', {'form': form})
