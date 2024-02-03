# Generated by Django 5.0.1 on 2024-02-03 11:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_listing', '0005_listedbooks_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='listedbooks',
            name='added_by_users',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), blank=True, default=['Rakshith'], size=None),
            preserve_default=False,
        ),
    ]