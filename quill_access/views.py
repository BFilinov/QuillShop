from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from quill_access.forms import RegisterForm


def register(request):
    if request.method == 'GET':
        return render(request, 'quill_access/register.html', {'form': RegisterForm(), 'form_url': reverse(register)})
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass
        return redirect('/')
