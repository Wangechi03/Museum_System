# Generated by Django 5.0.6 on 2024-07-02 14:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_visitor_booking_user_booking_ticket_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='total_price',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='num_tickets',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='booking',
            name='visitor_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2024, 7, 2))]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ticket_type',
            field=models.CharField(max_length=50),
        ),
    ]
