# Generated by Django 5.0.6 on 2024-07-11 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
