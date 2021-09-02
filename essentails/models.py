from django.db import models
from django.db.models.base import Model

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        default="description",
        null=True
    )
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0, decimal_places=3, max_digits=9)


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


class ItemBrand(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)