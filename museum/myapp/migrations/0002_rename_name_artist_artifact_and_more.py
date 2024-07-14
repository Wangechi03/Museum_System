# Generated by Django 5.0.6 on 2024-07-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='artifact',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='status',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='date_acquired',
        ),
        migrations.AddField(
            model_name='artifact',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='artist',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='phone',
            field=models.CharField(default=0.0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone2',
            field=models.CharField(blank=True, default=0.0, max_length=15),
            preserve_default=False,
        ),
    ]
