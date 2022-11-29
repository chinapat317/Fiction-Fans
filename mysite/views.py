from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    """Register a new user."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user=user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/fiction/')
        else:
            messages.add_message(request, messages.INFO, "Regiteration form is invalid")
        request.method = 'GET'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
