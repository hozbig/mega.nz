# Generated by Django 4.0.6 on 2022-07-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_activation',
            field=models.BooleanField(default=False),
        ),
    ]
