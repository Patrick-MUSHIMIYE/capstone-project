# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# from .forms import SignUpForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm  
# Create your views here.  
  
def signup(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('board_images')
    else:  
        form = CustomUserCreationForm()  
    context = {'form':form}  
    return render(request, 'signup.html', context)
