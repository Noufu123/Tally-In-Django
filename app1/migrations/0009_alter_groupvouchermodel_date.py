# Generated by Django 3.2.9 on 2022-08-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_groupvouchermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupvouchermodel',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]