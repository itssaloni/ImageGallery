# Generated by Django 4.2.5 on 2023-10-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_alter_place_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='PinCode',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='place',
            name='district',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='place',
            name='priority',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]