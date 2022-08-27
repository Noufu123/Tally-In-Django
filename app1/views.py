from importlib.resources import contents
from multiprocessing import context
from webbrowser import get
from django.shortcuts import render,redirect
from django.db.models import*
from app1.models import*

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

# my project view

def grouppage(request):
    data=groupcreatemodel.objects.all()
    context={'data':data}
    return render(request,'selectgroup.html',context)

# def ledgerpage(request,pk):
#     data=ledgeranalysismodel.objects.get(id=pk)
#     context={'data':data}
#     return render(request,'ledgeranalisys.html',context)

def ledgerpage(request,pk):
    ndata=ledgercreatemodel.objects.get(id=pk)
    data=ledgeranalysismodel.objects.filter(lpert=ndata)
    sum1=0
    sum2=0
    for a in data:
        sum1+=a.lpvalue
    for b in data:
        sum2+=b.svalue
    return render(request,'ledgeranalisys.html',{'data':data,'sum1':sum1,'sum2':sum2})

# def groupanalisys(request,pk):
#     data=groupanalysismodel.objects.get(id=pk)
#     context={'data':data}
#     return render(request,'groupanalisys.html',context)

def groupanalisys(request,pk):
    ndata=groupcreatemodel.objects.get(id=pk)
    data=groupanalysismodel.objects.filter(pert=ndata)
    sum1=0
    sum2=0
    for a in data:
        sum1+=a.pvalue
    for b in data:
        sum2+=b.svalue
    context={'data':data,'sum1':sum1,'sum2':sum2}
    return render(request,'groupanalisys.html',context)

def selectledgerpage(request):
    data=ledgercreatemodel.objects.all()
    context={'data':data}
    return render(request,'selectledger.html',context)

def groupitem(request,pk):
    ndata=groupanalysismodel.objects.get(id=pk)
    data=purchasevouchermodel.objects.filter(stockitem=ndata)
    sdata=salevouchermodel.objects.filter(stockitem=ndata)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for a in data:
        sum1+=a.quantity
    for b in data:
        sum2+=b.basicrate
    for c in data:
        sum3+=c.basicvalue
    for d in data:
        sum4+=d.addlcost
    for e in data:
        sum5+=e.totalvalue
    for f in data:
        sum6+=f.efsrate
    sum7=0
    sum8=0
    sum9=0
    sum10=0
    sum11=0
    sum12=0
    for g in sdata:
        sum7+=g.quantity
    for h in sdata:
        sum8+=h.basicrate
    for i in sdata:
        sum9+=i.basicvalue
    for j in sdata:
        sum10+=j.addlcost
    for k in sdata:
        sum11+=k.totalvalue
    for l in sdata:
        sum12+=l.efsrate
    return render(request,'groupitem.html',{'data':data,'ndata':ndata,'sdata':sdata,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8,'sum9':sum9,'sum10':sum10,'sum11':sum11,'sum12':sum12})

def ledgeritem(request,pk):
    ndata=ledgeranalysismodel.objects.get(id=pk)
    data=purchaseledgervouchermodel.objects.filter(lstockitem=ndata)
    sdata=salesledgervouchermodel.objects.filter(lstockitem=ndata)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for a in data:
        sum1+=a.lquantity
    for b in data:
        sum2+=b.lbasicrate
    for c in data:
        sum3+=c.lbasicvalue
    for d in data:
        sum4+=d.laddlcost
    for e in data:
        sum5+=e.ltotalvalue
    for f in data:
        sum6+=f.lefsrate
    sum7=0
    sum8=0
    sum9=0
    sum10=0
    sum11=0
    sum12=0
    for g in sdata:
        sum7+=g.lquantity
    for h in sdata:
        sum8+=h.lbasicrate
    for i in sdata:
        sum9+=i.lbasicvalue
    for j in sdata:
        sum10+=j.laddlcost
    for k in sdata:
        sum11+=k.ltotalvalue
    for l in sdata:
        sum12+=l.lefsrate
    return render(request,'ledgeritem.html',{'data':data,'ndata':ndata,'sdata':sdata,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8,'sum9':sum9,'sum10':sum10,'sum11':sum11,'sum12':sum12})

def creategroup(request):
    data=groupcreatemodel.objects.all()
    context={'data':data}
    return render(request,'groupcreate.html',context)

def ledgercreate(request):
    data=ledgercreatemodel.objects.all()
    cnt=countrymodel.objects.all()
    st=statemodel.objects.all()
    context={'data':data,'cnt':cnt,'st':st}
    return render(request,'ledgercreate.html',context)


def creategroupviews(request):
    if request.method=='POST':
        gpname=request.POST['name']
        gpalias=request.POST['alias']
        gpunder=request.POST['under']
        gpbehaves=request.POST['behaves']
        gpallocate=request.POST['allocate']
        data=groupcreatemodel(gname=gpname,galias=gpalias,gunder=gpunder,gbehaves=gpbehaves,gallocate=gpallocate)
        data.save()
        return redirect('grouppage')

def createledgerviews(request):
    if request.method=='POST':
        lpname=request.POST['name']
        lpalias=request.POST['alias']
        lpunder=request.POST['under']
        under=groupcreatemodel.objects.get(id=lpunder)
        lpmname=request.POST['mname']
        lpaddress=request.POST['address']
        lpstate=request.POST['state']
        lpcountry=request.POST['contry']
        lppincode=request.POST['pincode']
        lpbank=request.POST['bank']
        lppan=request.POST['pan']
        lpreg=request.POST['registrations']
        data=ledgercreatemodel(lname=lpname,lalias=lpalias,lunder=under,lmname=lpmname,laddress=lpaddress,lstate=lpstate,lcountry=lpcountry,lpincode=lppincode,lbank=lpbank,lpan=lppan,lreg=lpreg)
        data.save()
        return redirect('selectledgerpage')