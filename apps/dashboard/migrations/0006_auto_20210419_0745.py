# Generated by Django 3.1 on 2021-04-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210419_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]