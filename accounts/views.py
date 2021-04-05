from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print("Username: " + username)
            print("Password: " + password)
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')

    return render(request, 'accounts/login.html')

@unauthenticated_user
def SignUpView(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.info(request, user)
            return redirect('accCreated')
    
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

@login_required(login_url='login')
def homeView(request):
    return render(request, 'accounts/index.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def accCreated(request):
    return render(request, 'accounts/acccreated.html')