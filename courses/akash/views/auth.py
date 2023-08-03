from django.shortcuts import render, HttpResponse, redirect
from akash.models import Registration, Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import random


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        res_obj = Registration(
            username=username,
            email=email,
            password=password,
            password2=password2,
        )

        if password != password2:
            messages.error(request, "Password does not match")
            return redirect('SignupPage')
        elif username == "" or email == "" or password == "":
            return HttpResponse("Please fill these details")
        res_obj.save()

        messages.success(request, "Congrats! Your account has been created")
        return redirect("LoginPage")

    return render(request, 'course/signup.html')


def login(request):
    try:
        if request.method == "POST":
            lusername = request.POST.get('lusername')
            lpassword = request.POST.get('lpassword')

            user = Registration.objects.get(username=lusername)
            request.session['name'] = lusername
            messages.success(
                request, "Congrats! You are logged in successfully")

            return redirect("home")

        return render(request, 'course\login.html')
    except:
        messages.error(request, "Please enter valid details")
        return redirect("LoginPage")

    action = request.GET.get('action')
    context = {'action': action}
    return render(request, 'course\login.html', context=context)


def logout(request):
    request.session.clear()
    messages.success(request, "Logged out successfully")
    return redirect("LoginPage")


def forgetpage(request):
    try:
        if request.method == "POST":
            mob = request.POST.get("number")
            otp = random.randint(1000, 9999)
            print(mob)

            f_obj = Profile(mob=mob, otp=otp)

            f_obj.save()

            messages.success(request, "OTP has been sent")
            return redirect("home")

        return render(request, 'course/login.html')

    except:
        messages.error(request, "Sorry OTP not sent yet")
        return redirect("LoginPage")
