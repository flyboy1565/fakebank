# Generated by Django 2.2.5 on 2019-09-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(max_length=5),
        ),
    ]