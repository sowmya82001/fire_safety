from django.shortcuts import render, get_object_or_404
from .models import FireIncident, EmergencyResponse, FireTraining, ComplianceCheck
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from django.contrib.auth.models import User
from .models import OTPStorage
from django.core.mail import send_mail
import random
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Use the new form with CAPTCHA
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials or CAPTCHA, please try again.")
    else:
        form = LoginForm()  # Use the new form with CAPTCHA

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def forget_password_view(request):
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email)

            if users.exists():
                otp = str(random.randint(100000, 999999))

                # Update or create OTP for each user with the same email
                for user in users:
                    OTPStorage.objects.update_or_create(user=user, defaults={'otp': otp})

                # Send OTP email (only once as the email is the same for all users)
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}',
                    'admin@example.com',
                    [email],
                    fail_silently=False,
                )

                request.session['reset_email'] = email
                messages.success(request, "An OTP has been sent to your email address.")
                return redirect('reset_password')
            else:
                form.add_error('email', 'Email not found.')
    else:
        form = ForgetPasswordForm()

    return render(request, 'forget_password.html', {'form': form})

def reset_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            new_password = form.cleaned_data['new_password']
            email = request.session.get('reset_email')

            if email:
                # Get all users with the same email
                users = User.objects.filter(email=email)

                otp_valid = False

                for user in users:
                    try:
                        otp_obj = OTPStorage.objects.get(user=user)
                        if otp_obj.otp == otp:
                            user.set_password(new_password)
                            user.save()
                            otp_obj.delete()
                            otp_valid = True
                            break  # Exit loop after successful password reset
                    except OTPStorage.DoesNotExist:
                        continue

                if otp_valid:
                    messages.success(request, "Password reset successful. You can now log in.")
                    return redirect('login')
                else:
                    form.add_error('otp', 'Invalid OTP or expired session.')
            else:
                form.add_error(None, 'Session expired. Please try the password reset process again.')
    else:
        form = ResetPasswordForm()

    return render(request, 'reset_password.html', {'form': form})
    
def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, "home.html")

def fire_incidents(request):
    incidents = FireIncident.objects.all()
    return render(request, "safety/fire_incidents.html", {"incidents": incidents})

def emergency_response(request):
    responses = EmergencyResponse.objects.all()
    return render(request, "safety/emergency_response.html", {"responses": responses})

def fire_training(request):
    trainings = FireTraining.objects.all()
    return render(request, "safety/fire_training.html", {"trainings": trainings})

def compliance_checks(request):
    checks = ComplianceCheck.objects.all()
    return render(request, "safety/compliance_checks.html", {"checks": checks})
