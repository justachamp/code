from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.views import password_reset, password_reset_confirm

from django.shortcuts import render, redirect
from ui.backend.forms import KanaryPasswordResetForm


def login(request):
    ''' User authorization '''

    login = ''
    error = None
    if request.method == 'POST':
        login = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=login, password=password)
        if user and not user.is_anonymous():
            login_user(request, user)
            return redirect('main')
        else:
            error = 'Invalid username or password'

    return render(request, 'auth/login.html', {'login': login, 'error': error})


def csrf_failure(request, reason=""):
    return render(request, '403.html', {'login': '', 'error': reason}, status=403)


def reset_password(request):
    return password_reset(
        request=request,
        template_name='auth/reset_password.html',
        password_reset_form=KanaryPasswordResetForm,
        post_reset_redirect='reset_password_send'
    )


def reset_password_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(
        request=request,
        template_name='auth/reset_password_confirm.html',
        uidb64=uidb64,
        token=token,
        post_reset_redirect='auth-login'
    )


def reset_password_send(request):
    return render(request, 'auth/reset_password_send.html')
