# Generated by Django 3.2.12 on 2023-05-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230504_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
