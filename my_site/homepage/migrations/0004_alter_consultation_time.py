# Generated by Django 5.0.1 on 2024-01-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_rename_updated_at_consultation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
