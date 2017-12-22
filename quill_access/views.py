from django.shortcuts import render, reverse, redirect
from quill_access.forms import RegisterForm


def register(request):
    if request.method == 'GET':
        return render(request, 'quill_access/register.html',
                      {'form': RegisterForm(), 'form_url': reverse(register), 'current_user': request.user})
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save(True)
            request.user = register_form.value
        return redirect('/')


def profile(request):
    return render(request, 'quill_access/profile.html', {'user_data': request.user})


def login(request):
    return render(request, 'quill_access/profile.html')
