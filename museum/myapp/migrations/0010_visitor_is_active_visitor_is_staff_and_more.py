# Generated by Django 5.0.6 on 2024-07-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_visitor_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visitor',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visitor',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
