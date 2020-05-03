from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def SignupView(request):

    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'profiles/Signup.html', {'error': 'username taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'profiles/Signup.html', {'error': ' contraseña no coincide'})
    else:
        return render(request, 'profiles/Signup.html')

def LoginView(request):

    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user != None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'profiles/Login.html', {"error": 'Bad credentials provided!'})
    else:
        return render(request, 'profiles/Login.html')

def LogoutView(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')