# Generated by Django 4.0.6 on 2022-08-07 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='premium',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
