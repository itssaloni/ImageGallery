# Generated by Django 4.2.5 on 2023-10-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_category_image_delete_demotable_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
            ],
        ),
    ]
