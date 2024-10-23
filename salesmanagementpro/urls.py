"""
URL configuration for salesmanagementpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from salesmanagementapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('home',views.homepage,name='homepage'),
    path('registration',views.clientdata,name='registration'),
    path('contact',views.contactus,name = 'contactpage'),
    path('login',views.loginpage,name='loginpage'),
    path('about',views.aboutpage,name='aboutpage'),
    path('dashboard',views.dashboardpage,name = 'dashboard'),
    path('addnew',views.addnewprop,name='addnewproperty'),
    path('allproperty',views.allprop,name = 'allproperty'),
    path('logout',views.logoutuser,name = 'logout'),
    path('adminhoe',views.adminhome,name= 'adminhome'),
    path('adminabut',views.adminabout,name = 'adminabout'),
    path('appartments',views.appartment,name='appartment'),
    path('independent',views.independent,name='independent'),
    path('builderfloor',views.builderfloor,name='builderfloor'),
    path('villa',views.villas,name = 'villa'),
    path('addnewpropertytype',views.addnewproptype,name='addnewpropertytype'),
    path('addstatus',views.addstatus,name='addstatus'),
    path('propertyreport',views.display_properties,name = 'propertyreport'),
    path('statusreport',views.statusreports,name='statusreport'),
    path('propertytypereport',views.type_report,name='propertytypereport'),
    path('myaccount',views.my_account,name='myaccount'),
    path('changep',views.changepasswrd, name='changepassword'),
    path('delete/<id>',views.deletestudent,name = 'delete'),
    path('editprop/<int:id>', views.edit_property, name='editprop'),
    path('buyhome',views.buyhme,name='buyerhome'),
    path('buyabout',views.buyabout,name = 'buyerabout'),
    path('sellforgetpass',views.forgot_password,name='sellforgetpass'),
    path('buydash',views.buydashboard,name = 'buyerdashboard'),
    path('buyallprop',views.buyallprop,name='buyerallproperty'),
    path('buyappartment',views.buyappartment,name = 'buyerappartment'),
    path('buyindependentfloor',views.buyindependent,name = 'buyerindependent'),
    path('buybuilderfloor',views.buybuilder,name='buyerbuilderfloor'),
    path('buyvilla',views.buyvilla,name = 'buyervilla'),

    path('viewdetails/<id>',views.viewdetails,name='viewdetails'),
    path('sendenquiry/<id>',views.sendenquiry,name='sendenquiry'),
    path('enquiryreport',views.enquiryreport,name = 'enquiry_report'),
    path('viewflat/<id>',views.viewflat,name = 'viewflat'),
    path('customer_report',views.customer_report,name='customer_report'),
    path('myproperty',views.my_property,name = 'myproperty'),
    path('myaccpropdetails/<id>',views.myaccpropdetails,name = 'myaccpropdetails'),
    path('buyer_acc_details',views.buyer_acc_details,name='buyer_acc_details'),
    path('buyer_changepass',views.buyer_changepass,name='buyer_changepass'),


    path('post_property',views.post_property_view,name='post_property'),
    path('add_post_property/<property_id>',views.add_to_post_property,name='add_post_property'),
    path('del_from_post_property/<int:property_id>',views.del_from_post_property,name='del_from_post_property'),
    path('my_enquiry/',views.my_enquiry_view, name='my_enquiry_view'),
    path('delete_enquiry/<int:enquiry_id>/',views.delete_enquiry, name='delete_enquiry')




] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
