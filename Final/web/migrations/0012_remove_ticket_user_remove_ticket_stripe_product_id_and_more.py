# Generated by Django 4.1.6 on 2023-03-04 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_ticket_stripe_product_id_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='User',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='stripe_product_id',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]