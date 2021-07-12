# Generated by Django 3.2.3 on 2021-07-12 16:31

from django.db import migrations, models
import main.extras
import places.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20210624_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default/default.jpg', upload_to=main.extras.profile_picture),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_location',
            field=places.fields.PlacesField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_pic1',
            field=models.ImageField(upload_to=main.extras.get_pic_name, validators=[main.extras.validate_image]),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_pic2',
            field=models.ImageField(upload_to=main.extras.get_pic_name, validators=[main.extras.validate_image]),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_pic3',
            field=models.ImageField(upload_to=main.extras.get_pic_name, validators=[main.extras.validate_image]),
        ),
    ]