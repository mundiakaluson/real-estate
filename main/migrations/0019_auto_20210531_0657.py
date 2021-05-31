# Generated by Django 3.2.3 on 2021-05-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='average_review',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating_reviewed',
            field=models.FloatField(blank=True, choices=[('1.0', '1.0'), ('2.0', '2.0'), ('3.0', '3.0'), ('4.0', '4.0'), ('5.0', '5.0')], max_length=5, null=True),
        ),
    ]
