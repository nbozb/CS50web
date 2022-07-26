# Generated by Django 4.0.5 on 2022-07-11 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.PROTECT, related_name='itemsInCat', to='auctions.category'),
        ),
    ]
