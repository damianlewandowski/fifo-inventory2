# Generated by Django 3.0.2 on 2020-03-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200308_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
