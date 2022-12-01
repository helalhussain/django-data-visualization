from django.shortcuts import render,redirect
from .models import Chart
# Create your views here.

def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        data=Chart.objects.filter(trade_code=q)
        allData = Chart.objects.all()
    else:
        data = Chart.objects.all()
        allData = Chart.objects.all()
    return render(request,'index.html',{'data':data,'allData':allData})

def add(request):
    if request.method =='POST':
        add_date = request.POST.get('date')
        add_trade_code = request.POST.get('trade_code')
        add_high = request.POST.get('high')
        add_low = request.POST.get('low')
        add_open = request.POST.get('open')
        add_close = request.POST.get('close')
        add_volume = request.POST.get('volume')

        add= Chart()
        add.date = add_date
        add.trade_code =add_trade_code
        add.high = add_high
        add.low = add_low
        add.open = add_open
        add.close = add_close
        add.volume = add_volume
        add.save()
        return redirect('/')

    return render(request,'add.html', {})

def edit(request,id):
    edit =Chart.objects.get(id=id)
    return render(request,'edit.html',{'edit':edit})

def edited(request,id):
    eidit_date = request.POST.get('date')
    eidit_trade_code = request.POST.get('trade_code')
    eidit_high = request.POST.get('high')
    eidit_low =request.POST.get('low')
    eidit_open = request.POST.get('open')
    eidit_close = request.POST.get('close')
    eidit_volume = request.POST.get('volume')

    edit=Chart.objects.get(id=id)
    edit.date=eidit_date
    edit.trade_code=eidit_trade_code
    edit.high=eidit_high
    edit.low=eidit_low
    edit.open=eidit_open
    edit.close=eidit_close
    edit.volume=eidit_volume
    edit.save()
    return redirect('/')

def delete(request,id):
    delete=Chart.objects.get(id=id)
    delete.delete()
    return redirect('/')

