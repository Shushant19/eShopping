# Generated by Django 4.1 on 2022-09-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0005_order_dtls'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_dtls',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
