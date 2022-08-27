# Generated by Django 3.2.9 on 2022-08-25 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_delete_groupvouchermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='salevouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('basicrate', models.IntegerField()),
                ('basicvalue', models.IntegerField()),
                ('addlcost', models.IntegerField()),
                ('totalvalue', models.IntegerField()),
                ('efsrate', models.IntegerField()),
                ('stockitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.groupanalysismodel')),
                ('udergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.groupcreatemodel')),
            ],
        ),
        migrations.CreateModel(
            name='purchasevouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('basicrate', models.IntegerField()),
                ('basicvalue', models.IntegerField()),
                ('addlcost', models.IntegerField()),
                ('totalvalue', models.IntegerField()),
                ('efsrate', models.IntegerField()),
                ('stockitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.groupanalysismodel')),
                ('udergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.groupcreatemodel')),
            ],
        ),
    ]