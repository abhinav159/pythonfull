# Generated by Django 4.1.3 on 2022-12-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_seller_seller_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
