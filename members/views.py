from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There was an error logging in'))
            return redirect('login')
    return render(request, 'registration/login.html')




def register_user(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('Registration Successful'))
            return redirect('home')
         
           
    return render(request, 'registration/register_user.html', {'form':form})


def logout_user(request):
    logout(request)
    print("in logout function")
    messages.success(request, "Logged out successfully!")
    return redirect("login")