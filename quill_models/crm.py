from quill_models import products, auth
from django.db import models
from django.db.models import F


class Client(auth.User):
    pass


class ClientDiscount(models.Model):
    client = models.ForeignKey('Client', related_name='discounts')
    discount_amount = models.DecimalField(null=False, default=0)
    is_active = models.BooleanField(null=False, default=False)
    pass


class OrderCostManager(models.Manager):
    def get_queryset(self, **kwargs):
        pass


class OrderDiscountManager(models.Manager):
    def get_queryset(self, **kwargs):
        pass


class Order(models.Model):
    PAY_METHOD_CASH = ('C', 'Cash')
    PAY_METHOD_CARD = ('R', 'Credit Card')
    PAY_METHOD_BANK_INVOICE = ('I', 'Bank Invoice')
    __all_pay_methods = dict([PAY_METHOD_CASH, PAY_METHOD_CARD, PAY_METHOD_BANK_INVOICE])

    client = models.ForeignKey('Client', null=False)
    products = models.ManyToManyField('products.Product', null=False)
    total_cost = models.DecimalField(null=False)
    discount = models.DecimalField(null=True)
    order_date = models.DateField(null=True)
    manager = models.ForeignKey('auth.User', null=False)
    pay_method = models.CharField(max_length=1, null=True,
                                  choices=__all_pay_methods.items())
    is_paid = models.BooleanField(null=False, default=False)
