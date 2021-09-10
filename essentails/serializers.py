from typing import Text
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.utils import tree
from rest_framework import serializers
from essentails.models import User

# create serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user_name']
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.save()
        return instance

