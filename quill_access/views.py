from django.shortcuts import render, reverse, redirect
from quill_access.forms import RegisterForm,LoginForm
from django.contrib.auth import login as auth_login, logout as  auth_logout


def register(request):
    if request.method == 'GET':
        return render(request, 'quill_access/register.html',
                      {'form': RegisterForm(), 'form_url': reverse(register), 'current_user': request.user})
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        print('User register:', register_form.username)
        if register_form.is_valid():
            user = register_form.save(True)
            auth_login(request, user)
        return redirect('/')


def profile(request):
    return render(request, 'quill_access/profile.html', {'user_data': request.user})
