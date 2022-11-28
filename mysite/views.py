from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user=user)
            return redirect('/accounts/login')
    request.method = 'GET'
    messages.add_message(request, messages.INFO, "This username is already used.")
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})