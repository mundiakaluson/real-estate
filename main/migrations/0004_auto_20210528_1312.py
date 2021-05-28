# Generated by Django 3.2.3 on 2021-05-28 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210525_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_post_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('Mansion', 'Mansion'), ('Bungalow', 'Bungalow'), ('Cottage', 'Cottage'), ('Apartment', 'Apartment'), ('Condo', 'Condo'), ('Villa', 'Villa'), ('Ranch House', 'Ranch House'), ('Beach House', 'Beach House'), ('Hostel', 'Hostel'), ('Pent House', 'Pent House'), ('Bedsitter', 'Bedsitter'), ('Cabin', 'Cabin'), ('Castle', 'Castle'), ('Houseboats', 'Houseboats'), ('Ranch', 'Ranch'), ('Farm House', 'Farm House'), ('Office', 'Office'), ('Mall', 'Mall'), ('Store', 'Store'), ('Shop', 'Shop'), ('Hotel', 'Hotel'), ('Land', 'Land'), ('Plot', 'Plot')], max_length=64),
        ),
    ]