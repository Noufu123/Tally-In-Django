# Generated by Django 3.2.9 on 2022-08-25 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_purchasevouchermodel_salevouchermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ledgervouchermodel',
        ),
    ]