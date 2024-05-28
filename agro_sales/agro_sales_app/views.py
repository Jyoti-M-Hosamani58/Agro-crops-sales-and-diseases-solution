from django.shortcuts import render, redirect
from django.urls import reverse
from agro_sales_app.models import UserRegistration,UserLogin,OtpCode,AddAPMC,AddMarketPrice,AddDiseaseSolution,AddDiseaseMaster,AddBuyCrop,AddCrop,AddSellCrop

from django.core.files.storage import FileSystemStorage
import os
from agro_sales.settings import BASE_DIR
import random
import smtplib
import datetime


# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_home(request):
    return render(request,'admin_home.html')

def register(request):
    if request.method=="POST":
        utype=request.POST.get('t1')
        name=request.POST.get('t2')
        city= request.POST.get('t3')
        address= request.POST.get('t4')
        contact = request.POST.get('t5')
        email = request.POST.get('t6')
        password = request.POST.get('t7')
        ucount=UserRegistration.objects.filter(email=email).count()
        if ucount>=1:
            return render(request,'register.html',{'msg':'This is already exists'})
        else:
            UserRegistration.objects.create(name=name,city=city,address=address,contact=contact,email=email,password=password)
            UserLogin.objects.create(utype=utype, username=email, password=password)
            return render(request,'register.html',{'msg':'Thank you for registration'})
    return render(request,'register.html')

def register_view(request):
    userdata=UserRegistration.objects.all()
    return render(request,'register_view.html',{'userdata':userdata})

def register_edit(request,pk):
    rdata=UserRegistration.objects.filter(id=pk).values()
    if request.method=="POST":
        name = request.POST.get('t2')
        city = request.POST.get('t3')
        address = request.POST.get('t4')
        contact = request.POST.get('t5')
        email = request.POST.get('t6')
        UserRegistration.objects.filter(id=pk).update(name=name,city=city,address=address,contact=contact,email=email)
        base_url=reverse('register_view')
        return redirect(base_url)
    return render(request,'register_edit.html',{'rdata':rdata})

def forgotpass(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        request.session['username']=username
        ucount=UserLogin.objects.filter(username=username).count()
        if ucount>=1:
            otp=random.randint(1111,9999)
            OtpCode.objects.create(otp=otp,status='active')
            content="Your OTP is-"+str(otp)
            smtp_server=smtplib.SMTP_SSL('smtp.gmail.com',465)
            smtp_server.ehlo()
            smtp_server.login('pyatibrenuka@gmail.com', 'hzyeojargvuuyvnc')
            smtp_server.sendmail('pyatibrenuka@gmail.com', username, content)
            smtp_server.close()
            base_url=reverse('otp')
            return redirect(base_url)
        else:
            return render(request,'forgotpass.html',{'msg':'Invalid Username'})
    return render(request,'forgotpass.html')

def otp(request):
    if request.method=="POST":
        otp=request.POST.get('t1')
        count=OtpCode.objects.filter(otp=otp).count()
        if count>=1:
            base_url=reverse('reset')
            return redirect(base_url)
        else:
            return render(request,'otp.html',{'msg':'Invalid OTP'})
    return render(request,'otp.html')

def reset(request):
    username=request.session['username']
    if request.method=="POST":
        newpassword=request.POST.get('t1')
        confirmpassword=request.POST.get('t2')
        if newpassword==confirmpassword:
            UserLogin.objects.filter(username=username).update(password=newpassword)
            base_url=reverse('userlogin')
            return redirect(base_url)
        else:
            return render(request,'reset.html',{'msg':'newpassword and confirmpassword must be same'})
    return render(request,'reset.html')



def userlogin(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        password=request.POST.get('t2')
        request.session['username']=username
        ucount=UserLogin.objects.filter(username=username).count()
        if ucount>=1:
            udata=UserLogin.objects.get(username=username)
            upass=udata.password
            utype=udata.utype
            if password==upass:
                if utype=='buyer':
                    return render(request,'buyer_home.html')
                if utype=='seller':
                    return render(request,'seller_home.html')
                if utype=='farmer':
                    return render(request,'farmer_home.html')
                if utype=='admin':
                    return render(request,'admin_home.html')
                if utype=='apmc':
                    return render(request,'apmc_home.html')
            else:
                return render(request,'userlogin.html',{'msg':'Invalid Password'})
        else:
            return render(request,'userlogin.html',{'msg':'Invalid Username'})
    return render(request,'userlogin.html')

def addapmc(request):
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        district = request.POST.get('a2')
        city = request.POST.get('a3')
        location = request.POST.get('a4')
        establishment_year = request.POST.get('a5')
        AddAPMC.objects.create(apmc_name=apmc_name,district=district,city=city,location=location,establishment_year=establishment_year)
        return render(request,'addapmc.html',{'msg':' Added'})
    return render(request,'addapmc.html')

def apmc_view(request):
    userdata=AddAPMC.objects.all()
    return render(request,'apmc_view.html',{'userdata':userdata})

def apmc_del(request,pk):
    udata=AddAPMC.objects.get(id=pk)
    udata.delete()
    base_url=reverse('apmc_view')
    return redirect(base_url)

def apmc_edit(request,pk):
    rdata=AddAPMC.objects.filter(id=pk).values()
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        district = request.POST.get('a2')
        city = request.POST.get('a3')
        location = request.POST.get('a4')
        establishment_year = request.POST.get('a5')
        AddAPMC.objects.filter(id=pk).update(apmc_name=apmc_name,district=district,city=city,location=location,establishment_year=establishment_year)
        base_url=reverse('apmc_view')
        return redirect(base_url)
    return render(request,'apmc_edit.html',{'rdata':rdata})

def addcrops(request):
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        crop_name = request.POST.get('a2')
        quantity = request.POST.get('a3')
        cost = request.POST.get('a4')
        description = request.POST.get('a5')
        uom = request.POST.get('a6')
        stock = request.POST.get('a7')
        AddCrop.objects.create(apmc_name=apmc_name,crop_name=crop_name,quantity=quantity,cost=cost,description=description,uom=uom,stock=stock)
        return render(request,'addcrops.html',{'msg':' Added'})
    return render(request,'addcrops.html')

def crops_view(request):
    userdata=AddCrop.objects.all()
    return render(request,'crops_view.html',{'userdata':userdata})

def crops_del(request,pk):
    udata=AddCrop.objects.get(id=pk)
    udata.delete()
    base_url=reverse('crops_view')
    return redirect(base_url)

def crops_edit(request,pk):
    rdata=AddCrop.objects.filter(id=pk).values()
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        crop_name = request.POST.get('a2')
        quantity = request.POST.get('a3')
        cost = request.POST.get('a4')
        description = request.POST.get('a5')
        uom = request.POST.get('a6')
        stock = request.POST.get('a7')
        AddCrop.objects.filter(id=pk).update(apmc_name=apmc_name, crop_name=crop_name, quantity=quantity, cost=cost,description=description, uom=uom, stock=stock)
        base_url=reverse('crops_view')
        return redirect(base_url)
    return render(request, 'crops_edit.html',{'rdata':rdata})


def adddiseasemaster(request):
    if request.method=="POST":
        category = request.POST.get('a1')
        category_name = request.POST.get('a2')
        disease_name = request.POST.get('a3')
        symptoms = request.POST.get('a4')
        pesticides = request.POST.get('a5')
        AddDiseaseMaster.objects.create(category=category,category_name=category_name,disease_name=disease_name,symptoms=symptoms,pesticides=pesticides)
        return render(request,'adddiseasemaster.html',{'msg':' Added'})
    return render(request,'adddiseasemaster.html')

def disease_view(request,pk):
    udata=AddDiseaseSolution.objects.get(id=pk)
    category=udata.category_name
    userdata=AddDiseaseMaster.objects.filter(category_name=category).values()
    return render(request,'disease_view.html',{'userdata':userdata})

def disease_del(request,pk):
    udata=AddDiseaseMaster.objects.get(id=pk)
    udata.delete()
    base_url=reverse('disease_view')
    return redirect(base_url)

def diseasemaster_edit(request,pk):
    rdata=AddDiseaseMaster.objects.filter(id=pk).values()
    if request.method=="POST":
        category = request.POST.get('a1')
        category_name = request.POST.get('a2')
        disease_name = request.POST.get('a3')
        symptoms = request.POST.get('a4')
        pesticides = request.POST.get('a5')
        AddDiseaseMaster.objects.filter(id=pk).update(category=category, category_name=category_name, disease_name=disease_name,
                                        symptoms=symptoms, pesticides=pesticides)
        base_url=reverse('disease_view')
        return redirect(base_url)
    return render(request,'diseasemaster_edit.html',{'rdata':rdata})


def addmarketprice(request):
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        location = request.POST.get('a2')
        crop_name = request.POST.get('a3')
        qty = request.POST.get('a4')
        market_price = request.POST.get('a5')
        AddMarketPrice.objects.create(apmc_name=apmc_name,location=location,crop_name=crop_name,qty=qty,market_price=market_price)
        return render(request,'addmarketprice.html',{'msg':' Added'})
    return render(request,'addmarketprice.html')

def marketprice_view(request):
    userdata=AddMarketPrice.objects.all()
    return render(request,'marketprice_view.html',{'userdata':userdata})

def marketprice(request):
    userdata=AddMarketPrice.objects.all()
    return render(request,'marketprice.html',{'userdata':userdata})

def marketprice_del(request,pk):
    udata=AddMarketPrice.objects.get(id=pk)
    udata.delete()
    base_url=reverse('marketprice_view')
    return redirect(base_url)

def marketprice_edit(request,pk):
    rdata=AddMarketPrice.objects.filter(id=pk).values()
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        location = request.POST.get('a2')
        crop_name = request.POST.get('a3')
        qty = request.POST.get('a4')
        market_price = request.POST.get('a5')
        AddMarketPrice.objects.filter(id=pk).update(apmc_name=apmc_name,location=location,crop_name=crop_name,qty=qty,market_price=market_price)
        base_url=reverse('marketprice_view')
        return redirect(base_url)
    return render(request,'marketprice_edit.html',{'rdata':rdata})


def diseasemaster_edit(request,pk):
    rdata=AddDiseaseMaster.objects.filter(id=pk).values()
    if request.method=="POST":
        category = request.POST.get('a1')
        category_name = request.POST.get('a2')
        disease_name = request.POST.get('a3')
        symptoms = request.POST.get('a4')
        pesticides = request.POST.get('a5')
        AddDiseaseMaster.objects.filter(id=pk).update(category=category, category_name=category_name, disease_name=disease_name,
                                        symptoms=symptoms, pesticides=pesticides)
        base_url=reverse('disease_view')
        return redirect(base_url)
    return render(request,'diseasemaster_edit.html',{'rdata':rdata})

def adddiseasesolution(request,cat):
    username=request.session['username']
    if cat=="Fruits":
        cdata=AddDiseaseMaster.objects.filter(category=cat).values()
    elif cat=="Crop":
        cdata = AddDiseaseMaster.objects.filter(category=cat).values()
    else:
        cdata = AddDiseaseMaster.objects.filter(category=cat).values()

    if request.method=="POST" and request.FILES['myfile']:
        uname = request.POST.get('a1')
        upload_file = request.POST.get('a2')
        category = request.POST.get('a3')
        category_name= request.POST.get('a4')


        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        upload_file_url=fs.url(filename)
        path=os.path.join(BASE_DIR,'/media/'+filename)

        AddDiseaseSolution.objects.create(uname=uname,upload_file=myfile,category=category,category_name=category_name)
        return render(request,'adddiseasesolution.html',{'msg':' Added'})
    return render(request,'adddiseasesolution.html',{'cat':cat,'username':username,'cdata':cdata})


def solution_view(request):
    username=request.session['username']
    userdata=AddDiseaseSolution.objects.filter(uname=username).values()
    return render(request,'solution_view.html',{'userdata':userdata})

def solution_del(request,pk):
    udata=AddDiseaseSolution.objects.get(id=pk)
    udata.delete()
    base_url=reverse('solution_view')
    return redirect(base_url)

def solution_edit(request,pk):
    rdata=AddDiseaseSolution.objects.filter(id=pk).values()
    if request.method == "POST" and request.FILES['myfile']:
        uname = request.POST.get('a1')
        upload_file = request.POST.get('a2')
        category = request.POST.get('a3')
        symptoms = request.POST.get('a4')
        disease_name = request.POST.get('a5')
        pesticides = request.POST.get('a6')
        status = request.POST.get('a7')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)
        AddDiseaseSolution.objects.filter(id=pk).update(uname=uname, upload_file=myfile, category=category, symptoms=symptoms,
                                          disease_name=disease_name, pesticides=pesticides, status=status)
        base_url=reverse('solution_view')
        return redirect(base_url)
    return render(request,'solution_edit.html',{'rdata':rdata})

def addbuycrop(request):
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        farmer_id = request.POST.get('a2')
        crop_id = request.POST.get('a3')
        quantity = request.POST.get('a4')
        uom = request.POST.get('a5')
        cost = request.POST.get('a6')
        total_cost = request.POST.get('a7')
        buy_date = request.POST.get('a8')
        status = request.POST.get('a9')
        pay_status = request.POST.get('a10')
        AddBuyCrop.objects.create(apmc_name=apmc_name,farmer_id=farmer_id,crop_id=crop_id,quantity=quantity,uom=uom,cost=cost,total_cost=total_cost,buy_date=buy_date,status=status,pay_status=pay_status)
        return render(request,'addbuycrop.html',{'msg':' Added'})
    return render(request,'addbuycrop.html')

def buycrop_view(request):
    uid = request.session['username']
    userdata = AddBuyCrop.objects.filter(farmer_id=uid).values()
    return render(request,'buycrop_view.html',{'userdata':userdata})

def buycrop_del(request,pk):
    udata=AddBuyCrop.objects.get(id=pk)
    udata.delete()
    base_url=reverse('buycrop_view')
    return redirect(base_url)

def buycrop_edit(request,pk):
    rdata=AddBuyCrop.objects.filter(id=pk).values()
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        farmer_id = request.POST.get('a2')
        crop_id = request.POST.get('a3')
        quantity = request.POST.get('a4')
        uom = request.POST.get('a5')
        cost = request.POST.get('a6')
        total_cost = request.POST.get('a7')
        buy_date = request.POST.get('a8')
        status = request.POST.get('a9')
        pay_status = request.POST.get('a10')
        AddBuyCrop.objects.filter(id=pk).update(apmc_name=apmc_name,farmer_id=farmer_id,crop_id=crop_id,quantity=quantity,uom=uom,cost=cost,total_cost=total_cost,buy_date=buy_date,status=status,pay_status=pay_status)
        base_url=reverse('buycrop_view')
        return redirect(base_url)
    return render(request,'buycrop_edit.html',{'rdata':rdata})

def buy_crop(request):
    pdata=AddCrop.objects.all()
    return render(request,'buy_crop.html',{'pdata':pdata})

def enter_quantity(request,pk):
    uid=request.session['username']
    now=datetime.datetime.now()
    buy_date=now.strftime("%Y-%m-%d")
    udata=AddCrop.objects.get(id=pk)
    cropname=udata.crop_name
    apmc=udata.apmc_name
    uom=udata.uom
    cost=int(udata.cost)
    if request.method=="POST":
        qty=int(request.POST.get('a1'))
        total=qty*cost
        AddBuyCrop.objects.create(apmc_name=apmc,farmer_id=uid,crop_name=cropname,crop_id=pk,quantity=qty,uom=uom,cost=cost,total_cost=total,status='pending',pay_status='pending',buy_date=buy_date)
        return render(request,'enter_quantity.html',{'msg':'Order has been placed successfully'})

    return render(request,'enter_quantity.html')

def croprequest_buy(request):
    userdata=AddBuyCrop.objects.all()
    return render(request,'croprequest_buy.html',{'userdata':userdata})

def buycrop_accept(request,pk):
    AddBuyCrop.objects.filter(id=pk).update(status='accepted')
    base_url=reverse('croprequest_buy')
    return redirect(base_url)

def buying_status(request):
    uid=request.session['username']
    userdata=AddBuyCrop.objects.filter(farmer_id=uid).values()
    return render(request,'buying_status.html',{'userdata':userdata})

def payamount(request,pk):
    pdata=AddBuyCrop.objects.get(id=pk)
    total=pdata.total_cost
    if request.method=="POST":
        AddBuyCrop.objects.filter(id=pk).update(pay_status='paid')
        return render(request, 'payamount.html', {'msg': 'Payment has been done successfully'})

    return render(request,'payamount.html',{'total':total})

def croprequest_sell(request):
    userdata=AddSellCrop.objects.all()
    return render(request,'croprequest_sell.html',{'userdata':userdata})

def selling_status(request):
    uid = request.session['username']
    userdata = AddSellCrop.objects.filter(farmer_id=uid).values()
    return render(request,'selling_status.html',{'userdata':userdata})

def sellcrop_accept(request,pk):
    AddSellCrop.objects.filter(id=pk).update(status='accepted')
    base_url=reverse('croprequest_sell')
    return redirect(base_url)


def invoice(request,pk):
    now=datetime.datetime.now()
    bill_date=now.strftime("%d-%m-%Y")
    udata=AddBuyCrop.objects.get(id=pk)
    uid=udata.farmer_id
    crop_id=udata.crop_id
    cdata=AddCrop.objects.get(id=crop_id)
    crop_name=cdata.crop_name
    qty=udata.quantity
    uom=udata.uom
    cost=udata.cost
    total=udata.total_cost

    udata1=UserRegistration.objects.get(email=uid)
    name=udata1.name
    address=udata1.address


    AddBuyCrop.objects.filter(id=pk).update(pay_status='paid')
    return render(request,'invoice.html',{'bno':pk,'bill_date':bill_date,'name':name,'address':address,'crop_name':crop_name,'qty':qty,'uom':uom,'cost':cost,'total':total})

def addsellcrop(request):
    uid = request.session['username']
    now=datetime.datetime.now()
    sdate=now.strftime("%Y-%m-%d")
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        farmer_id = request.POST.get('a2')
        crop_name = request.POST.get('a3')
        quantity = request.POST.get('a4')
        uom = request.POST.get('a5')
        selling_date = request.POST.get('a6')

        AddSellCrop.objects.create(apmc_name=apmc_name,farmer_id=farmer_id,crop_name=crop_name,quantity=quantity,uom=uom,selling_date=selling_date,status='pending')
        return render(request,'addsellcrop.html',{'msg':' Added','uid':uid,'sdate':sdate})
    return render(request,'addsellcrop.html',{'uid':uid,'sdate':sdate})

def sellcrop_view(request):
    userdata=AddSellCrop.objects.all()
    return render(request,'sellcrop_view.html',{'userdata':userdata})

def sellcrop_del(request,pk):
    udata=AddSellCrop.objects.get(id=pk)
    udata.delete()
    base_url=reverse('sellcrop_view')
    return redirect(base_url)


def sellcrop_edit(request,pk):
    rdata=AddSellCrop.objects.filter(id=pk).values()
    if request.method=="POST":
        apmc_name = request.POST.get('a1')
        farmer_id = request.POST.get('a2')
        crop_name = request.POST.get('a3')
        quantity = request.POST.get('a4')
        uom = request.POST.get('a5')
        selling_date = request.POST.get('a6')
        status = request.POST.get('a7')
        AddSellCrop.objects.filter(id=pk).update(apmc_name=apmc_name,farmer_id=farmer_id,crop_name=crop_name,quantity=quantity,uom=uom,selling_date=selling_date,status=status)
        base_url=reverse('sellcrop_view')
        return redirect(base_url)
    return render(request,'sellcrop_edit.html',{'rdata':rdata})






