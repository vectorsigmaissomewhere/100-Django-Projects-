from .models import CustomUser
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        middle_name = request.POST.get('middlename')
        last_name = request.POST.get('lastname')
        mobile = request.POST.get('phonenumber')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Check if passwords match
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This Email address is already taken.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # Create and save the user
        user = CustomUser(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            mobile=mobile
        )
        user.set_password(password)
        user.save()

        # Optionally, log the user in immediately after registration
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Redirect to a home page or dashboard

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')  # Redirect to login page

    # Handling GET request with query parameters
    email = request.GET.get('email', '')
    first_name = request.GET.get('firstname', '')
    middle_name = request.GET.get('middlename', '')
    last_name = request.GET.get('lastname', '')
    mobile = request.GET.get('phonenumber', '')

    context = {
        'email': email,
        'firstname': first_name,
        'middlename': middle_name,
        'lastname': last_name,
        'phonenumber': mobile,
    }

    return render(request, 'register.html', context)

def login(request):
    return render(request,'login.html')
