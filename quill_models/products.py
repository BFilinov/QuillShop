from django.db import models
from django.db.models import F
import datetime

DATE_MIN_VALUE = datetime.datetime(1970, 1, 1)


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=300, null=False)
    parent_category = models.ForeignKey('ProductCategory', null=True, related_name='sub_categories',
                                        on_delete=models.PROTECT)


class ProductPriceManager(models.Manager):
    def get_query_set(self, **kwargs):
        now = datetime.datetime.now()
        qs = super().get_queryset().filter(date_from__le=now, date_to__ge=now)
        if len(kwargs.items()) > 0:
            qs = qs.filter(**kwargs)
        return qs


class Product(models.Model):
    product_title = models.CharField(max_length=500, null=False)
    product_description = models.CharField(max_length=2500, null=False)
    product_category = models.ForeignKey('ProductCategory', null=False, on_delete=models.PROTECT,
                                         related_name='products')
    product_price = ProductPriceManager().get_queryset(product=F('id')).first()
    objects = models.Manager()


class ProductPrice(models.Model):
    product = models.ForeignKey('Product', null=False, on_delete=models.PROTECT)
    price = models.DecimalField(null=False, default=1000)
    date_from = models.DateField(auto_now=True, null=False, default=DATE_MIN_VALUE)
    date_to = models.DateField(auto_now=False, null=False, default=datetime.datetime.max)
