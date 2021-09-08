from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Form(models.Model):
    FORM_STATUS = [
        ('LIVE', 'Live'),
        ('CLOSED', 'Closed'),
        ('DONE', 'Done')
    ]
    form_name = models.CharField(max_length=200)
    form_status = models.CharField(
        choices=FORM_STATUS,
        default=None,
        max_length=20
    )
    form_description = models.TextField(
        default="description_form",
        null=True
    )


class Item(models.Model):
    form = models.ForeignKey(Form, related_name='items', on_delete=models.CASCADE)
    item_category = models.CharField(max_length=100, default="CATEGORY")
    item_name = models.CharField(max_length=200)


class Brand(models.Model):
    item = models.ForeignKey(Item, related_name='brands', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=200)
    brand_description = models.TextField(
        default="description_brand",
        null=True
    )
    brand_is_available = models.BooleanField(default=None, blank=True)


class User(models.Model):
    user_name = models.CharField(max_length=200)
    items = models.ManyToManyField(
        Item,
        through='UserItem',
        through_fields=['user', 'item']
    )


class UserForm(models.Model):
    user = models.ForeignKey(User, related_name="user_forms", on_delete=models.CASCADE)
    form = models.ForeignKey(Form, related_name='form_users', on_delete=models.CASCADE)
    updates = models.TextField(max_length=400)

class UserItem(models.Model):
    user = models.ForeignKey(User, related_name='user_items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='item_user', on_delete=models.CASCADE)
    brand = models.OneToOneField(Brand, related_name='brand', on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField(default=0)
    quantity_delivered = models.IntegerField(default=0)
    quantity_available = models.IntegerField(blank=True, null=True)
    price_per_item = models.DecimalField(
                default=0,
                decimal_places=3,
                max_digits=9
            )


