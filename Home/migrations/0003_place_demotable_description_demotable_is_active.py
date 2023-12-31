# Generated by Django 4.2.5 on 2023-09-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='demotable',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='demotable',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
