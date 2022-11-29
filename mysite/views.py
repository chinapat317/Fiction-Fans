from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
    """Register a new user."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
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
