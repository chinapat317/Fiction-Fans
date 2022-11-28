from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_pw = form.cleaned_data.get('password')
            try:
                user = authenticate(username=username, password=raw_pw)
                login(request, user=user)
                return redirect('/accounts/login')
            except:
                messages.add_message(request, messages.INFO, "This username is already used.")
        else:
            messages.add_message(request, messages.INFO, "Your registration form is invalid please redo it again.")
    request.method = 'GET'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})