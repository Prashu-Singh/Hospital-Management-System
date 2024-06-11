from django.contrib import admin
from .models import *

# Register your models here.

# class DoctorAdmin(admin.ModelAdmin):
#     list_display = ['dr_name','age','mob_no','speciality','gender','date_of_join','address','salary']
#     list_filter = ['speciality']
admin.site.register(Doctor)

# class PatientAppoAdmin(admin.ModelAdmin):
#     list_display = ['patient_name','patient_mob','gender','age','doctor','address','date_appo','status']
#     list_filter = ['date_appo']
admin.site.register(PatientAppo)
admin.site.register(Contactus)
admin.site.register(Admit)
