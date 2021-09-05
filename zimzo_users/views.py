from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from zimzo_users.forms import RegisterUserForm

# Create your views here.


def register_users(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterUserForm()

    return render(request, 'zimzo_users/register_users.html', {'form': form})


def user_login(request):

    return render(request, 'zimzo_users/user_login.html')
