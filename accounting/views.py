from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounting.forms import UserRegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('user-home')
    if request.POST:
        username = request.POST['email']
        username = username.strip().loawecase()
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user-home')
        else:
            if User.objects.filter(email=username, is_active=False).exists():
                return render(request, 'wait-for-accept.html')

            data = {
                'errors': 'Incorrect email or password!'
            }
            return render(request, 'login.html', data)

    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('user-login')


def signup_view(request):
    errors = None
    if request.POST:

        email = request.POST['email']
        email = email.strip().loawecase()
        if User.objects.filter(email=email).exists():
            errors = 'This email has already been registered!'
        else:

            form = UserRegisterForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                user = User.objects.create(username=email, email=email,
                                           first_name=cleaned_data['first_name'], is_active=False)
                user.set_password(cleaned_data['password1'])
                user.save()

                return render(request, 'wait-for-accept.html')
            else:
                errors = form.errors

    data = {
        'errors': errors,
    }

    return render(request, 'signup.html', data)
