# Generated by Django 3.2.9 on 2022-08-25 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_delete_ledgervouchermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='salesledgervouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldate', models.DateField(auto_now_add=True)),
                ('lname', models.CharField(max_length=250)),
                ('lquantity', models.IntegerField()),
                ('lbasicrate', models.IntegerField()),
                ('lbasicvalue', models.IntegerField()),
                ('laddlcost', models.IntegerField()),
                ('ltotalvalue', models.IntegerField()),
                ('lefsrate', models.IntegerField()),
                ('lstockitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ledgeranalysismodel')),
                ('ludergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ledgercreatemodel')),
            ],
        ),
        migrations.CreateModel(
            name='purchaseledgervouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldate', models.DateField(auto_now_add=True)),
                ('lname', models.CharField(max_length=250)),
                ('lquantity', models.IntegerField()),
                ('lbasicrate', models.IntegerField()),
                ('lbasicvalue', models.IntegerField()),
                ('laddlcost', models.IntegerField()),
                ('ltotalvalue', models.IntegerField()),
                ('lefsrate', models.IntegerField()),
                ('lstockitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ledgeranalysismodel')),
                ('ludergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ledgercreatemodel')),
            ],
        ),
    ]
