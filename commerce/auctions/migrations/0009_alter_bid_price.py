# Generated by Django 4.0.5 on 2022-07-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_starting_price_alter_bid_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]