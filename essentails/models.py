from django.db import models
from django.db.models.base import Model

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        default="description_brand",
        null=True
    )
    is_available = models.BooleanField(default=None)


class Item(models.Model):
    ITEM_CATEGORIES = [
        ('SNACKS', 'Snacks'),
        ('BISCUITS', 'Biscuits'),
        ('CHOCOLATES', 'Chocolates'),
        ('HEALTH', 'Health')
    ]
    name = models.CharField(max_length=200)
    category = models.CharField(
        choices=ITEM_CATEGORIES,
        default='Snacks',
        max_length=20
    )
    brands = models.ManyToManyField(
        Brand,
        through='ItemBrand',
        through_fields=('item', 'brand')
    )
    is_available = models.BooleanField(default=None)


class ItemBrand(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(
        default=0,
        decimal_places=3,
        max_digits=9
    )
    


class Form(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=None)
    updates = models.TextField(
        default="description_form",
        null=True
    )
    is_available = models.BooleanField(default=None)

class FormItem(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
