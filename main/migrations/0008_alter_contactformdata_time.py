# Generated by Django 3.2.8 on 2021-10-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211028_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformdata',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
