"""agro_sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from agro_sales_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),

    path('userlogin', views.userlogin, name='userlogin'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('register',views.register,name='register'),
    path('register_view',views.register_view,name='register_view'),
    path('register_edit/<int:pk>', views.register_edit, name='register_edit'),

    path('forgotpass', views.forgotpass, name='forgotpass'),
    path('otp', views.otp, name='otp'),
    path('reset', views.reset, name='reset'),

    path('addapmc', views.addapmc, name='addapmc'),
    path('apmc_view', views.apmc_view, name='apmc_view'),
    path('apmc_del/<int:pk>', views.apmc_del, name='apmc_del'),
    path('apmc_edit/<int:pk>', views.apmc_edit, name='apmc_edit'),

    path('addcrops', views.addcrops, name='addcrops'),
    path('crops_view', views.crops_view, name='crops_view'),
    path('crops_del/<int:pk>', views.crops_del, name='crops_del'),
    path('crops_edit/<int:pk>', views.crops_edit, name='crops_edit'),

    path('addbuycrop', views.addbuycrop, name='addbuycrop'),
    path('buycrop_view', views.buycrop_view, name='buycrop_view'),
    path('buycrop_del/<int:pk>', views.buycrop_del, name='buycrop_del'),
    path('buycrop_edit/<int:pk>', views.buycrop_edit, name='buycrop_edit'),

    path('addmarketprice', views.addmarketprice, name='addmarketprice'),
    path('marketprice_view', views.marketprice_view, name='marketprice_view'),
    path('marketprice_del/<int:pk>', views.marketprice_del, name='marketprice_del'),
    path('marketprice_edit/<int:pk>', views.marketprice_edit, name='marketprice_edit'),

    path('adddiseasesolution/<str:cat>',views.adddiseasesolution,name='adddiseasesolution'),
    path('solution_view', views.solution_view, name='solution_view'),
    path('solution_del/<int:pk>', views.solution_del, name='solution_del'),
    path('solution_edit/<int:pk>', views.solution_edit, name='solution_edit'),

    path('adddiseasemaster',views.adddiseasemaster,name='adddiseasemaster'),
    path('disease_view/<int:pk>', views.disease_view, name='disease_view'),
    path('disease_del/<int:pk>', views.disease_del, name='disease_del'),
    path('diseasemaster_edit/<int:pk>', views.diseasemaster_edit, name='diseasemaster_edit'),

    path('enter_quantity/<int:pk>', views.enter_quantity, name='enter_quantity'),
    path('buy_crop', views.buy_crop, name='buy_crop'),
    path('croprequest_buy', views.croprequest_buy, name='croprequest_buy'),
    path('buycrop_accept/<int:pk>', views.buycrop_accept, name='buycrop_accept'),
    path('buying_status', views.buying_status, name='buying_status'),
    path('payamount/<int:pk>', views.payamount, name='payamount'),
    path('croprequest_sell', views.croprequest_sell, name='croprequest_sell'),
    path('selling_status', views.selling_status, name='selling_status'),
    path('sellcrop_accept/<int:pk>', views.sellcrop_accept, name='sellcrop_accept'),
    path('invoice/<int:pk>', views.invoice, name='invoice'),

    path('addsellcrop',views.addsellcrop,name='addsellcrop'),
    path('sellcrop_view', views.sellcrop_view, name='sellcrop_view'),
    path('sellcrop_del/<int:pk>', views.sellcrop_del, name='sellcrop_del'),
    path('sellcrop_edit/<int:pk>', views.sellcrop_edit, name='sellcrop_edit'),

    path('marketprice', views.marketprice_view, name='marketprice'),

]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
