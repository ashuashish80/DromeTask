# Generated by Django 4.1.7 on 2023-03-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
