# Generated by Django 4.0.6 on 2022-08-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_level_user_user_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='max_upload_file',
            field=models.PositiveIntegerField(default=1073741824),
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=3),
        ),
    ]
