from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('User Created')
                return redirect('accounts:login')
        else:
            messages.info(request, 'Passwords not matching...')
            return redirect('accounts:signup')
        # return redirect('/')

    else:
        # the following is a GET request
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(usermame=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('blogs:index')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('accounts:login')
