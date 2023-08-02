# Generated by Django 4.1.6 on 2023-08-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_rename_status_mockinterview_public_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='extracontentlink',
            name='status',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='status',
        ),
        migrations.RemoveField(
            model_name='videoanswerlink',
            name='status',
        ),
        migrations.AddField(
            model_name='comment',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='extracontentlink',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videoanswerlink',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mockinterview',
            name='grade',
            field=models.CharField(choices=[('Не указан', 'Не указан'), ('Trainee', 'Trainee'), ('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default='Не указан', max_length=100),
        ),
        migrations.AlterField(
            model_name='mockinterview',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.CharField(choices=[('Не указан', 'Не указан'), ('Trainee', 'Trainee'), ('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default='Не указан', max_length=100),
        ),
    ]
