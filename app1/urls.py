from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('grouppage',views.grouppage,name='grouppage'),
    path('ledgerpage',views.ledgerpage,name="ledgerpage"),
    path('groupanalisys',views.groupanalisys,name="groupanalisys"),
    path('selectledgerpage',views.selectledgerpage,name="selectledgerpage"),
    path('groupitem',views.groupitem,name="groupitem"),
    path('ledgeritem',views.ledgeritem,name="ledgeritem"),
    path('creategroup',views.creategroup,name="creategroup"),
    path('ledgercreate',views.ledgercreate,name="ledgercreate"),


]