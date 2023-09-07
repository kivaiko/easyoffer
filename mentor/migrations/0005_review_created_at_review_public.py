# Generated by Django 4.1.6 on 2023-09-05 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0004_alter_review_rating_alter_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='review',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
