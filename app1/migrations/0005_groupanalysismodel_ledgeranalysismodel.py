# Generated by Django 3.2.9 on 2022-08-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20220821_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='groupanalysismodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perticular', models.CharField(max_length=250)),
                ('pquatity', models.IntegerField()),
                ('prate', models.IntegerField()),
                ('pvalue', models.IntegerField()),
                ('squatity', models.IntegerField()),
                ('srate', models.IntegerField()),
                ('svalue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ledgeranalysismodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lperticular', models.CharField(max_length=250)),
                ('lpquatity', models.IntegerField()),
                ('lprate', models.IntegerField()),
                ('lpvalue', models.IntegerField()),
                ('lsquatity', models.IntegerField()),
                ('lsrate', models.IntegerField()),
                ('svalue', models.IntegerField()),
            ],
        ),
    ]
