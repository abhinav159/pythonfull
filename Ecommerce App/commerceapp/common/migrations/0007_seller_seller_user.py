# Generated by Django 4.1.3 on 2022-12-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_seller_seller_accno_alter_seller_seller_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_user',
            field=models.CharField(default='', max_length=30),
        ),
    ]