from django.urls import path
from . import views

urlpatterns = [
    path('',views.homee,name='home'),
    path('adddr',views.add_doctor,name='add_doctor'),
    path('addpat',views.add_appoinment,name='add_appoinment'),
    path('drdata',views.showdrdata,name='drdata'),
    path('appodata',views.showdappodata,name='appodata'),
    path('upddoctor/<int:id>',views.upd_doctor,name='upddoctor'),
    path('deldoctor/<int:id>',views.del_doctor,name='deldoctor'),
    path('updappoinmnet/<int:id>',views.upd_appoinment,name='updappoinment'),
    path('delappoinment/<int:id>',views.del_appoinment,name='delappoinment'),
    path('approve/<id>',views.approve, name='approve'),
    path('reject/<id>',views.reject,name='reject'),
    path('signup',views.sign_up,name='signup'),
    path('loginuser',views.log_in ,name='loginuser'),
    path('logoutuser',views.log_out,name='logoutuser'),
    path('contactus',views.contactus,name='contactus'),
    path('contactlist',views.showcontactlist,name='contactlist'),
    path('delcontact/<int:id>',views.del_contact,name='delcontact'),
    path('addadmit',views.addadmitted_patient,name='addadmit'),
    path('admitdata',views.showdadmited_data,name='admitdata'),
    path('updadmit/<int:id>',views.upd_admit,name='updadmit'),
    path('deladmit/<id>',views.del_admit,name='deladmit'),
]