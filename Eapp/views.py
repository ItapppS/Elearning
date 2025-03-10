from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import PhnUser, SubDomain  # Import the model

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
    return render(request, 'Obstacle_avoidance_car.html')

def profile(request): 
    return render(request, 'profile.html')

def cart(request): 
    return render(request, 'cart.html')

def base(request): 
    return render(request, 'base.html')

def home(request):
    domains = TechnologyDomain.objects.all()
    return render(request, 'home.html', {'domains': domains})

def bionic_hand(request):
    return render(request, 'bionic_hand.html')

def asterbot(request):
    return render(request, 'asterbot.html')

def navbarr(request):
    return render(request, 'navbarr.html')


def doghead(request):
    return render(request, 'doghead.html')

def realtimeclock(request):
    return render(request, 'Realtimeclock.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import PhnUser  

def register(request):
    if request.method == "POST":
        user_data = {
            "first_name": request.POST.get("first_name", "").strip(),
            "last_name": request.POST.get("last_name", "").strip(),
            "username": request.POST.get("username", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "password": request.POST.get("password", "").strip(),
            "confirm_password": request.POST.get("confirm_password", "").strip(),
            "age": request.POST.get("age", "").strip(),
            "address": request.POST.get("address", "").strip(),
           "mobile_no": request.POST.get("mobile_no", "").strip(),
 
        }
 
        print("Received Data:", user_data)  # Debugging
 
        if not all(user_data.values()):
            messages.error(request, "All fields are required.")
            return redirect("register")
 
        if "@" not in user_data["email"] or "." not in user_data["email"]:
            messages.error(request, "Invalid email format.")
            return redirect("register")
 
        if user_data["password"] != user_data["confirm_password"]:
            messages.error(request, "Passwords do not match!")
            return redirect("register")
 
        if PhnUser.objects.filter(email=user_data["email"]).exists():
            messages.error(request, "Email already registered!")
            return redirect("register")
 
        if PhnUser.objects.filter(username=user_data["username"]).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")
 
        if PhnUser.objects.filter(mobile_no=user_data["mobile_no"]).exists():
            messages.error(request, "Mobile number already registered!")
            return redirect("register")
 
        try:
            user_data["age"] = int(user_data["age"])
            if not (10 <= user_data["age"] <= 100):
                messages.error(request, "Age must be between 10 and 100.")
                return redirect("register")
        except ValueError:
            messages.error(request, "Age must be a valid number.")
            return redirect("register")
 
        user_data["password"] = make_password(user_data["password"])
 
        try:
            user = PhnUser(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                username=user_data["username"],
                email=user_data["email"],
                password=user_data["password"],
                age=user_data["age"],
                address=user_data["address"],
                mobile_no=user_data["mobile_no"],
            )
            user.save()
 
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("verify_email")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect("register")
 
    return render(request, "register.html")





def doghead(request):
    return render(request, 'dog.html')


from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = PhnUser.objects.get(username=username)  # Sirf username check kar

            # Password hash check karne ke liye `check_password()` use kar
            if check_password(password, user.password):
                request.session["user_id"] = user.username  # Session set kar diya
                messages.success(request, "Login Successful!")
                return redirect("home")  # Yahan 'home' page ka naam hai, tu change kar sakta hai
            else:
                messages.error(request, "Invalid Credentials")
        except PhnUser.DoesNotExist:
            messages.error(request, "Invalid Credentials")

    return render(request, "login.html")  # Login page render karna


def logout(request):
    request.session.flush()  # Session delete karna
    messages.success(request, "Logged out successfully!")
    return redirect("login")  # Redirect to login page


import requests

def verify_email(request):
    if request.method == "POST":
        email = request.POST.get("email").strip()

        # ✅ Check if email exists in the database
        if PhnUser.objects.filter(email=email).exists():
            messages.success(request, "Email Verified Successfully!")

            # ✅ Step 1: Web3Forms API request
            web3forms_url = "https://api.web3forms.com/submit"
            data = {
                "access_key": "4eb3e0df-598e-49e8-84bf-efe9c73fa04d",
                "email": email,
                "subject": "Email Verified",
                "message": f"The email {email} has been verified successfully!"
            }

            try:
                response = requests.post(web3forms_url, data=data, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                messages.error(request, f"Email verification failed: {str(e)}")
                return redirect("verify_email")

            # ✅ Step 2: Redirect to login page after successful verification
            return redirect("login")  
        else:
            messages.error(request, "Email not found. Please register first.")
            return redirect("verify_email")

    return render(request, "verification.html")


# def NA(request):
#     return render(request, 'NA.html')

from .models import TechnologyDomain, Project

def NA(request):
    domains = TechnologyDomain.objects.all()
    return render(request, 'NA.html', {'domains': domains})

def technology_detail(request, slug):
    domain = get_object_or_404(TechnologyDomain, slug=slug)
    return render(request, 'technology_detail.html', {'domain': domain})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})


def subdomain_detail(request, slug):
    subdomain = get_object_or_404(SubDomain, slug=slug)
    return render(request, 'subdomain_detail.html', {'subdomain': subdomain})



