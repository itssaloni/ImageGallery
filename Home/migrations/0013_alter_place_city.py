# Generated by Django 4.2.5 on 2023-10-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_alter_place_pincode_alter_place_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
