# Generated by Django 3.0.4 on 2020-10-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fApp', '0007_auto_20201015_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
