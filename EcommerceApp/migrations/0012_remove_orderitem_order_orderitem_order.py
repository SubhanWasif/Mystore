# Generated by Django 4.0.6 on 2022-07-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0011_remove_orderitem_order_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ManyToManyField(null=True, to='EcommerceApp.order'),
        ),
    ]