from typing import Text
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.utils import tree
from rest_framework import serializers
from essentails.models import Brand, Form, Item, User, UserItem


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'brand_name', 'brand_description', 'brand_is_available', 'item']

    def create(self, validated_data):
        item = validated_data.pop('item')
        return Brand.objects.create(item_id=item.id, **validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.save()
        return instance

class ItemSerializer(serializers.ModelSerializer):

    brands = BrandSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = [
            'id', 'item_name', 'item_category', 'brands', 'form'
        ]

    def create(self, validated_data):
        form = validated_data.pop('form')
        return Item.objects.create(form_id=form.id, **validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('description', instance.category)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class FormSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Form
        fields = [
            'id', 'form_name',
            'form_status', 'form_description', 'items'
        ]

    def create(self, validated_data):
        print("validated_data: ", validated_data)
        return Form.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user_name']
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.form_updates = validated_data.get('form_updates', instance.form_updates)
        instance.delivered_quantity = validated_data.get('delivered_quantity', instance.delivered_quantity)
        instance.save()
        return instance

class UserItemInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserItem
        fields = [
            'id', 'user', 'item',
            'brand', 'quantity_available',
            'price_per_item', 'quantity_ordered',
            'quantity_delivered'
        ]
    
    def create(self, validated_data):
        user = validated_data.pop('user')
        item = validated_data.pop('item')
        brand = validated_data.pop('brand')
        return UserItem.objects.create(
            user_id=user.id, item_id=item.id, brand_id=brand.id, **validated_data
        )
    
    def update(self, instance, validated_data):
        instance.quantity_available = validated_data.get('quantity_available', instance.quantity_available)
        instance.price_per_item = validated_data.get('price_per_item', instance.price_per_item)
        instance.quantity_ordered = validated_data.get('quantity_ordered', instance.quantity_ordered)
        instance.quantity_delivered = validated_data.get('quantity_delivered', instance.quantity_delivered)
        instance.save()
        return instance