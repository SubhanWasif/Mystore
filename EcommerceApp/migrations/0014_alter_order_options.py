# Generated by Django 4.0.6 on 2022-08-07 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0013_remove_orderitem_order_orderitem_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-date_ordered',)},
        ),
    ]
