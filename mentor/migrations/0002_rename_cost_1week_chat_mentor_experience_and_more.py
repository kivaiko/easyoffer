# Generated by Django 4.1.6 on 2023-08-04 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='cost_1week_chat',
            new_name='experience',
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='free_15min',
            new_name='public',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='cost_4h',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='cost_8h',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='status',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='years_experience',
        ),
    ]
