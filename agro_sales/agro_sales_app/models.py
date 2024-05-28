from django.db import models

class UserLogin(models.Model):
    username=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=30)

class UserRegistration(models.Model):
    utype = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

class OtpCode(models.Model):
    otp = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)

class AddAPMC(models.Model):
    apmc_name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    establishment_year = models.CharField(max_length=10)

class AddMarketPrice(models.Model):
    apmc_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    crop_name = models.CharField(max_length=50)
    qty = models.CharField(max_length=50)
    market_price = models.CharField(max_length=100)

class AddDiseaseSolution(models.Model):
    uname = models.CharField(max_length=30,null=True)
    upload_file = models.CharField(max_length=50,null=True)
    category = models.CharField(max_length=50,null=True)
    category_name = models.CharField(max_length=50,null=True)

class AddDiseaseMaster(models.Model):
    category = models.CharField(max_length=30)
    category_name = models.CharField(max_length=50)
    disease_name = models.CharField(max_length=50)
    symptoms = models.CharField(max_length=50)
    pesticides = models.CharField(max_length=100)

class AddBuyCrop(models.Model):
    apmc_name = models.CharField(max_length=30,null=True)
    farmer_id = models.CharField(max_length=50,null=True)
    crop_id = models.CharField(max_length=50,null=True)
    crop_name = models.CharField(max_length=50,null=True)
    quantity = models.CharField(max_length=100,null=True)
    uom = models.CharField(max_length=10,null=True)
    cost = models.CharField(max_length=50,null=True)
    total_cost = models.CharField(max_length=30,null=True)
    buy_date = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=30,null=True)
    pay_status = models.CharField(max_length=30,null=True)

class AddCrop(models.Model):
    apmc_name = models.CharField(max_length=30,null=True)
    crop_name = models.CharField(max_length=50,null=True)
    quantity = models.CharField(max_length=50,null=True)
    cost = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    uom = models.CharField(max_length=50,null=True)
    stock = models.CharField(max_length=30,null=True)

class AddBuyCrop(models.Model):
    apmc_name = models.CharField(max_length=30,null=True)
    farmer_id = models.CharField(max_length=50,null=True)
    crop_id = models.CharField(max_length=50,null=True)
    crop_name = models.CharField(max_length=50,null=True)
    quantity = models.CharField(max_length=100,null=True)
    uom = models.CharField(max_length=10,null=True)
    cost = models.CharField(max_length=50,null=True)
    total_cost = models.CharField(max_length=30,null=True)
    buy_date = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=30,null=True)
    pay_status = models.CharField(max_length=30,null=True)

class AddSellCrop(models.Model):
    apmc_name = models.CharField(max_length=30,null=True)
    farmer_id = models.CharField(max_length=50,null=True)
    crop_name = models.CharField(max_length=50,null=True)
    quantity = models.CharField(max_length=50,null=True)
    uom = models.CharField(max_length=100,null=True)
    selling_date = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)




# Create your models here.
