# Generated by Django 3.2.3 on 2021-07-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='registered_as',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
