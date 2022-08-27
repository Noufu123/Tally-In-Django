from datetime import date
from operator import mod
from django.db import models

# Create your models here.


class groupcreatemodel(models.Model):
    gname=models.CharField(max_length=250)
    galias=models.CharField(max_length=250)
    gunder=models.CharField(max_length=250)
    gbehaves=models.CharField(max_length=250)
    gallocate=models.CharField(max_length=250)

class ledgercreatemodel(models.Model):
    lname=models.CharField(max_length=250)
    lalias=models.CharField(max_length=250)
    lunder=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    lmname=models.CharField(max_length=250)
    laddress=models.CharField(max_length=250)
    lstate=models.CharField(max_length=250)
    lcountry=models.CharField(max_length=250)
    lpincode=models.CharField(max_length=250)
    lbank=models.CharField(max_length=250)
    lpan=models.CharField(max_length=250)
    lreg=models.CharField(max_length=250)

class groupanalysismodel(models.Model):
    pert=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    perticular=models.CharField(max_length=250)
    pquatity=models.IntegerField()
    prate=models.IntegerField()
    pvalue=models.IntegerField()
    squatity=models.IntegerField()
    srate=models.IntegerField()
    svalue=models.IntegerField()

class ledgeranalysismodel(models.Model):
    lpert=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    lperticular=models.CharField(max_length=250)
    lpquatity=models.IntegerField()
    lprate=models.IntegerField()
    lpvalue=models.IntegerField()
    lsquatity=models.IntegerField()
    lsrate=models.IntegerField()
    svalue=models.IntegerField()

# class groupvouchermodel(models.Model):
#     stockitem=models.ForeignKey(groupanalysismodel,on_delete=models.CASCADE)
#     udergroup=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
#     date=models.DateField(auto_now_add=True)
#     perticular=models.CharField(max_length=250)
#     name=models.CharField(max_length=250)
#     quantity=models.IntegerField()
#     basicrate=models.IntegerField()
#     basicvalue=models.IntegerField()
#     addlcost=models.IntegerField()
#     totalvalue=models.IntegerField()
#     efsrate=models.IntegerField()


# class ledgervouchermodel(models.Model):
#     lstockitem=models.ForeignKey(ledgeranalysismodel,on_delete=models.CASCADE)
#     ludergroup=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
#     ldate=models.DateField(auto_now_add=True)
#     lperticular=models.CharField(max_length=250)
#     lname=models.CharField(max_length=250)
#     lquantity=models.IntegerField()
#     lbasicrate=models.IntegerField()
#     lbasicvalue=models.IntegerField()
#     laddlcost=models.IntegerField()
#     ltotalvalue=models.IntegerField()
#     lefsrate=models.IntegerField()

class purchasevouchermodel(models.Model):
    stockitem=models.ForeignKey(groupanalysismodel,on_delete=models.CASCADE)
    udergroup=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    # perticular=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    quantity=models.IntegerField()
    basicrate=models.IntegerField()
    basicvalue=models.IntegerField()
    addlcost=models.IntegerField()
    totalvalue=models.IntegerField()
    efsrate=models.IntegerField()

class salevouchermodel(models.Model):
    stockitem=models.ForeignKey(groupanalysismodel,on_delete=models.CASCADE)
    udergroup=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    # perticular=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    quantity=models.IntegerField()
    basicrate=models.IntegerField()
    basicvalue=models.IntegerField()
    addlcost=models.IntegerField()
    totalvalue=models.IntegerField()
    efsrate=models.IntegerField()

class purchaseledgervouchermodel(models.Model):
    lstockitem=models.ForeignKey(ledgeranalysismodel,on_delete=models.CASCADE)
    ludergroup=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    ldate=models.DateField(auto_now_add=True)
    # lperticular=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    lquantity=models.IntegerField()
    lbasicrate=models.IntegerField()
    lbasicvalue=models.IntegerField()
    laddlcost=models.IntegerField()
    ltotalvalue=models.IntegerField()
    lefsrate=models.IntegerField()

class salesledgervouchermodel(models.Model):
    lstockitem=models.ForeignKey(ledgeranalysismodel,on_delete=models.CASCADE)
    ludergroup=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    ldate=models.DateField(auto_now_add=True)
    # lperticular=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    lquantity=models.IntegerField()
    lbasicrate=models.IntegerField()
    lbasicvalue=models.IntegerField()
    laddlcost=models.IntegerField()
    ltotalvalue=models.IntegerField()
    lefsrate=models.IntegerField()

class countrymodel(models.Model):
    name=models.CharField(max_length=250)

class statemodel(models.Model):
    cname=models.ForeignKey(countrymodel,on_delete=models.CASCADE)
    sname=models.CharField(max_length=250)