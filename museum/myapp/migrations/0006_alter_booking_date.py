# Generated by Django 5.0.6 on 2024-07-03 03:10

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2024, 7, 3))]),
        ),
    ]
