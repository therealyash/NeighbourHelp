# Generated by Django 3.2.6 on 2025-02-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
