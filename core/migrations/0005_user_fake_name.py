# Generated by Django 3.2.12 on 2023-05-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_comment_quality'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fake_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nickname'),
        ),
    ]