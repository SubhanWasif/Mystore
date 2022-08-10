# Generated by Django 4.0.6 on 2022-07-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0008_alter_order_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
