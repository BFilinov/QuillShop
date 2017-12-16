from django.shortcuts import render, redirect


def home(request):
    return render(request, 'quill_app/index.html')


def cart(request):
    return render(request, 'quill_app/index.html')


def contacts(request):
    return render(request, 'quill_app/index.html')


def profile(request):
    return render(request, 'quill_app/index.html')
