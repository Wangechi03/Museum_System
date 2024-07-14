# Generated by Django 5.0.6 on 2024-07-11 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_visitor_is_active_visitor_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='visitor',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
