# Generated by Django 3.2.3 on 2021-06-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_rename_reviews_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewed_user',
            field=models.CharField(max_length=256),
        ),
    ]
