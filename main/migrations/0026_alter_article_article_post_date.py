# Generated by Django 3.2.3 on 2021-06-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_article_article_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_post_date',
            field=models.DateField(max_length=64),
        ),
    ]
