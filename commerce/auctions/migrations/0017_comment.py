# Generated by Django 4.0.5 on 2022-07-19 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auctionitem_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commentsOnListing', to='auctions.auctionitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='myComments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]