from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD

# Create your views here.

=======
from django.contrib import messages
>>>>>>> master

def signup(request):
    """Register a new user."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            username = form.cleaned_data.get("username")
            raw_passwd = form.cleaned_data.get("password")
            user = authenticate(username=username,password=raw_passwd)
            login(request, user)
            form.save()
        return redirect("/accounts/login")
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
=======
            user = form.save()
            login(request, user=user)
            return redirect('/fiction/')
    request.method = 'GET'
    messages.add_message(request, messages.INFO, "Regiteration form is invalid")
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
>>>>>>> master
