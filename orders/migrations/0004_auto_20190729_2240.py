# Generated by Django 2.0.3 on 2019-07-29 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190729_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_fullfilled',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_placed',
            field=models.DateTimeField(blank=True),
        ),
    ]
