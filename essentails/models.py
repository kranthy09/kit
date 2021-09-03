from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices

# Create your models here.


class Form(models.Model):
    FORM_STATUS = [
        ('LIVE', 'Live'),
        ('CLOSED', 'Closed'),
        ('DONE', 'Done')
    ]
    name = models.CharField(max_length=200)
    status = models.CharField(
        choices=FORM_STATUS,
        default=None,
        max_length=20
    )
    updates = models.TextField(
        default="description_form",
        null=True
    )


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
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=None)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(
        default=0,
        decimal_places=3,
        max_digits=9
    )
