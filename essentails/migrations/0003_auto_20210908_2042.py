# Generated by Django 3.2.6 on 2021-09-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essentails', '0002_alter_item_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='quantity_delivered',
        ),
        migrations.AddField(
            model_name='useritem',
            name='quantity_delivered',
            field=models.IntegerField(default=0),
        ),
    ]