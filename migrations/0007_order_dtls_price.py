# Generated by Django 4.1 on 2022-09-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0006_order_dtls_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_dtls',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
