from django.forms import forms
from quill_models import crm, products


class ProductForm(forms.Form):
    class Meta:
        model = products.Product
        fields = ['__all']


class CartForm(forms.Form):
    class Meta:
        model = crm.Order
        fields = [
            'client',
            'product'
        ]
