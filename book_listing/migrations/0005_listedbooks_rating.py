# Generated by Django 5.0.1 on 2024-02-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_listing', '0004_listedbooks_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='listedbooks',
            name='rating',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]