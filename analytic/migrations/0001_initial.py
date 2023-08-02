# Generated by Django 4.1.6 on 2023-08-01 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField(default=1)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.profession')),
            ],
            options={
                'db_table': 'anaytics_skills',
            },
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField(default=1)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.profession')),
            ],
            options={
                'db_table': 'anaytics_keywords',
            },
        ),
    ]
