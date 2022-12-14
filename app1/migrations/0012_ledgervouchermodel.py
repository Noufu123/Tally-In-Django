# Generated by Django 3.2.9 on 2022-08-25 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_groupvouchermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ledgervouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldate', models.DateField(auto_now_add=True)),
                ('lperticular', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('lquantity', models.IntegerField()),
                ('lbasicrate', models.IntegerField()),
                ('lbasicvalue', models.IntegerField()),
                ('laddlcost', models.IntegerField()),
                ('ltotalvalue', models.IntegerField()),
                ('lefsrate', models.IntegerField()),
                ('lstockitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.groupanalysismodel')),
                ('ludergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.groupcreatemodel')),
            ],
        ),
    ]
