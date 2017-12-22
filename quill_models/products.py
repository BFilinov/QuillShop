from django.db import models


class ProductCategory(models.Model):
    class Meta:
        app_label = 'quill_app'

    category_name = models.CharField(max_length=300, null=False)
    parent_category = models.ForeignKey('ProductCategory', null=True, related_name='sub_categories',
                                        on_delete=models.PROTECT)


class Product(models.Model):
    class Meta:
        app_label = 'quill_app'

    product_title = models.CharField(max_length=500, null=False)
    product_description = models.CharField(max_length=2500, null=False)
    product_category = models.ForeignKey('ProductCategory', null=False, on_delete=models.PROTECT,
                                         related_name='products')
    product_price = models.DecimalField(null=False, default=100, decimal_places=2, max_digits=12)
    image_url = models.CharField(max_length=2000, null=True)
    objects = models.Manager()
