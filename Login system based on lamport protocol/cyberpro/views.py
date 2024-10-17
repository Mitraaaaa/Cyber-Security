from django.shortcuts import render
from .models import UserProfile
from cyberpro.forms import UserSignupForm, UserLoginForm, lamport_hash


def homepage(request):
    return render(request, 'homepage.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'sign_up.html',
                   {'form': form, 'message': 'Successfully signed up'})
            # return HttpResponse('home')
        else:
            return render(request, 'sign_up.html',
                          {'form': form, 'error_message': 'Duplicate username or password'})

    else:
        form = UserSignupForm()

    return render(request, 'sign_up.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserProfile.objects.get(username=username)
            except UserProfile.DoesNotExist:
                return render(request, 'login.html',
                              {'form': form, 'error_message': 'User not found'})

            # Verify Lamport hash for login
            hashed_password = lamport_hash(user.n_value, password)
            if hashed_password == user.password:

                if user.n_value == 0:
                    return render(request, 'login.html',
                                  {'form': form, 'error_message': 'Number of valid logins has ended'})

                user.n_value = user.n_value - 1
                new_hashed_password = lamport_hash(user.n_value, password)
                user.password = new_hashed_password
                user.save()
                return render(request, 'login.html',
                              {'form': form, 'message': 'Successfully logged in'})
            else:
                return render(request, 'login.html',
                              {'form': form, 'error_message': 'Password verification failed'})
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})
