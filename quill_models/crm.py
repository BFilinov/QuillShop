from quill_models import products
from quill_access import models as qa_models
from django.db import models


class Client(qa_models.User):
    class Meta:
        app_label = 'quill_app'

    client_company_name = models.CharField(max_length=300, null=False)
    client_inn = models.CharField(max_length=12, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ClientDiscount(models.Model):
    class Meta:
        app_label = 'quill_app'

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


class OrderProductAmount(models.Model):
    class Meta:
        app_label = 'quill_app'

    order = models.ForeignKey('Order', related_name='product_amounts')
    product = models.ForeignKey('products.Product')
    amount = models.IntegerField(null=False, default=1)


class OrderProductDisplayManager(models.Manager):
    def get_queryset(self, **kwargs):
        pass


class Order(models.Model):
    class Meta:
        app_label = 'quill_app'

    PAY_METHOD_CASH = ('C', 'Cash')
    PAY_METHOD_CARD = ('R', 'Credit Card')
    PAY_METHOD_BANK_INVOICE = ('I', 'Bank Invoice')
    __all_pay_methods = dict([PAY_METHOD_CASH, PAY_METHOD_CARD, PAY_METHOD_BANK_INVOICE])

    client = models.ForeignKey('Client', null=False)
    total_cost = models.DecimalField(null=False)
    discount = models.DecimalField(null=True)
    order_date = models.DateField(null=True)
    manager = models.ForeignKey('auth.User', null=False)
    pay_method = models.CharField(max_length=1, null=True,
                                  choices=__all_pay_methods.items())
    is_paid = models.BooleanField(null=False, default=False)
    display_products = OrderProductDisplayManager.get_queryset()
