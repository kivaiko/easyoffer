from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm


def register(request):
    return render(request, 'register.html')


def oauth(request):
    print(request.body)
    return HttpResponse("OK")
    # return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Редирект на страницу после успешной авторизации
                return redirect('index.html')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'login.html', {'form': form})