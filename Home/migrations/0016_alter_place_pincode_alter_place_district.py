# Generated by Django 4.2.5 on 2023-10-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_alter_place_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='PinCode',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='district',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
