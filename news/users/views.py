from django.shortcuts import render, HttpResponseRedirect
from .forms import AuthenticatedUser
from django.urls import reverse
from django.contrib import auth

# Create your views here.
def login_user(request):
    error = None
    if request.method == 'POST':
        form = AuthenticatedUser(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
        else:
            error = form.non_field_errors()

    form = AuthenticatedUser()

    context = {
        'error': error,
        'form': form
    }
    return render(request, 'users/login_form.html', context)
