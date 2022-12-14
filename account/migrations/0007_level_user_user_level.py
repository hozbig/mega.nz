# Generated by Django 4.0.6 on 2022-08-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
                ('max_upload', models.PositiveIntegerField(default=2147483648)),
                ('max_upload_file', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('max_divide', models.PositiveIntegerField(default=20)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.level'),
        ),
    ]
