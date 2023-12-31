# Generated by Django 4.1.3 on 2022-12-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_customer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=30)),
                ('seller_address', models.CharField(max_length=30)),
                ('seller_phone', models.CharField(max_length=30)),
                ('seller_email', models.BigIntegerField()),
                ('seller_companyname', models.CharField(max_length=100)),
                ('seller_accholder', models.CharField(default='', max_length=30)),
                ('seller_ifsc', models.CharField(max_length=10)),
                ('seller_branch', models.CharField(max_length=10)),
                ('seller_accno', models.CharField(max_length=10)),
                ('seller_password', models.CharField(max_length=10)),
                ('seller_pic', models.ImageField(upload_to='seller/')),
            ],
        ),
    ]
