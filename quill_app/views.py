from django.shortcuts import render, redirect
from quill_models.products import Product


def index(request):
    query = Product.objects.all()
    return render(request, 'quill_app/index.html', {'prod': query, 'current_user': request.user})


def product(request):
    if request.method == 'GET':
        prod_id = request['prod_id']
        item = Product.objects.get(id=prod_id)
        return render(request, 'quill_app/productview.html', {'item': item})


