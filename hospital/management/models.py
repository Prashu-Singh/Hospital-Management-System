from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator,MinLengthValidator
from datetime import date

# Create your models here.

gen_choice =(('Male','Male'),('Female','Female'),('Trans','Trans'))
sep_choice =(('Orthopedics','Orthopedics'),('Internal Medicine','Internal Medicine'),('Obstetrics and Gynecology','Obstetrics and Gynecology'),('Dermatology','Dermatology'),('Pediatrics','Pediatrics'),('Radiology','Radiology'),('General Surgery','General Surgery'),('Ophthalmology','Ophthalmology'))


class Doctor(models.Model):
    dr_name = models.CharField(max_length=20)
    age = models.CharField(max_length=3,validators=[RegexValidator("^\S[0-9]{0,3}$")])
    mob_no = models.CharField(max_length=10,validators=[RegexValidator("^(\+\d{1,3}[- ]?)?\d{10}$",message="Only numbers allowed"),MinLengthValidator(10,"10-digit allowed")])
    gender = models.CharField(max_length=20,choices=gen_choice)
    speciality = models.CharField(max_length=100,choices=sep_choice)
    date_of_join = models.DateField()
    salary = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.dr_name
    
class PatientAppo(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=20)
    patient_mob = models.CharField(max_length=10,validators=[RegexValidator("^(\+\d{1,3}[- ]?)?\d{10}$",message="Only numbers allowed"),MinLengthValidator(10,"10-digit allowed")])
    gender = models.CharField(max_length=20,choices=gen_choice,)
    age = models.CharField(max_length=3,validators=[RegexValidator("^\S[0-9]{0,3}$")])
    doctor = models.ForeignKey(Doctor,on_delete=models.DO_NOTHING,null=True,blank=True)
    address = models.TextField()
    date_appo = models.DateField()
    status = models.CharField(max_length=30,default='pending')
    
    def __str__(self):
        return self.patient_name

class Admit(models.Model):
    patient = models.ForeignKey(PatientAppo,on_delete=models.CASCADE)
    room_no = models.CharField(max_length=5)
    contact_no = models.CharField(max_length=10,validators=[RegexValidator("^(\+\d{1,3}[- ]?)?\d{10}$",message="Only numbers allowed"),MinLengthValidator(10,"10-digit allowed")])
    age = models.CharField(max_length=3,validators=[RegexValidator("^\S[0-9]{0,3}$")])
    gender = models.CharField(max_length=20,choices=gen_choice,)
    address = models.TextField()
    admit_date = models.DateField(default=date.today)
    discharge_date = models.DateField(default=date.today)
    deposite_fee = models.IntegerField(default=0)

    def __str__(self) :
        return self.patient.patient_name
   
class Contactus(models.Model):
    cname =  models.CharField(max_length=20)
    cmob = models.CharField(max_length=10,validators=[RegexValidator("^(\+\d{1,3}[- ]?)?\d{10}$",message="Only numbers allowed"),MinLengthValidator(10,"10-digit allowed")])
    cdate = models.DateField(default=date.today)
    cemail = models.EmailField()
    cmsg = models.TextField()

    def __str__(self) :
        return self.cname