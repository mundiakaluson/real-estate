# Generated by Django 3.2.3 on 2021-05-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_userinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='city',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='continent_code',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='continent_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='country_code',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='country_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='dma_code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='is_in_european_union',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='region',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='time_zone',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]