from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login') # maybe to change (to login page)
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})
