# Generated by Django 3.2.3 on 2021-07-01 19:12

from django.db import migrations, models
import main.extras


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
    ]