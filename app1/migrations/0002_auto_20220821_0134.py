# Generated by Django 3.2.9 on 2022-08-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupcreatemodel',
            name='gunder',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='groupnamemodel',
        ),
    ]
