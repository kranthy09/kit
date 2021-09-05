from django.db.models.enums import Choices
from rest_framework import serializers
from essentails.models import Form


class FormSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    status = serializers.ChoiceField(choices=Form.FORM_STATUS, default=None)
    description = serializers.CharField(default="description_form")

    def create(self, validated_data):
        return Form.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance