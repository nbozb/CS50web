# Generated by Django 4.0.5 on 2022-07-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auctionitem_posted_auctionitem_updated_bid_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='current_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]