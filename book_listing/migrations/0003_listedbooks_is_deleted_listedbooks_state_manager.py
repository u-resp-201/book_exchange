# Generated by Django 5.0.1 on 2024-02-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_listing', '0002_listedbooks_added_by_user_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='listedbooks',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listedbooks',
            name='state_manager',
            field=models.IntegerField(default=-100),
        ),
    ]