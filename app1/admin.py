from django.contrib import admin
from app1.models import *
# Register your models here.

@admin.register(groupcreatemodel)
class grpadmin(admin.ModelAdmin):
    list_display = ('id','gname','galias','gunder','gbehaves','gallocate')
  
@admin.register(groupanalysismodel)
class grpanalisysadmin(admin.ModelAdmin):
    list_display = ('id','pert','perticular','pquatity','prate','pvalue','squatity','srate','svalue')

@admin.register(ledgeranalysismodel)
class ledgeranalisysadmin(admin.ModelAdmin):
    list_display = ('id','lpert','lperticular','lpquatity','lprate','lpvalue','lsquatity','lsrate','svalue')

# @admin.register(groupvouchermodel)
# class groupvoucheradmin(admin.ModelAdmin):
#     list_display = ('id','stockitem','udergroup','date','perticular','name','quantity','basicrate','basicvalue','addlcost','totalvalue','efsrate')


# @admin.register(ledgervouchermodel)
# class ledgervoucheradmin(admin.ModelAdmin):
#     list_display = ('id','lstockitem','ludergroup','ldate','lperticular','lname','lquantity','lbasicrate','lbasicvalue','laddlcost','ltotalvalue','lefsrate')

@admin.register(purchasevouchermodel)
class purchasevoucheradmin(admin.ModelAdmin):
    list_display = ('id','stockitem','udergroup','date','name','quantity','basicrate','basicvalue','addlcost','totalvalue','efsrate')

@admin.register(salevouchermodel)
class salevoucheradmin(admin.ModelAdmin):
    list_display = ('id','stockitem','udergroup','date','name','quantity','basicrate','basicvalue','addlcost','totalvalue','efsrate')

@admin.register(purchaseledgervouchermodel)
class purchaseledgervoucheradmin(admin.ModelAdmin):
    list_display = ('id','lstockitem','ludergroup','ldate','lname','lquantity','lbasicrate','lbasicvalue','laddlcost','ltotalvalue','lefsrate')

@admin.register(salesledgervouchermodel)
class salesledgervoucheradmin(admin.ModelAdmin):
    list_display = ('id','lstockitem','ludergroup','ldate','lname','lquantity','lbasicrate','lbasicvalue','laddlcost','ltotalvalue','lefsrate')

@admin.register(countrymodel)
class countryadmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(statemodel)
class stateadmin(admin.ModelAdmin):
    list_display = ('id','cname','sname')