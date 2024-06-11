from django import forms
from .models import *

# gen_choice =(('Male','Male'),('Female','Female'),('Trans','Trans'))
# sep_choice =(('Orthopedics','Orthopedics'),('Internal Medicine','Internal Medicine'),('Obstetrics and Gynecology','Obstetrics and Gynecology'),('Dermatology','Dermatology'),('Pediatrics','Pediatrics'),('Radiology','Radiology'),('General Surgery','General Surgery'),('Ophthalmology','Ophthalmology'))


class Doctoform(forms.ModelForm):
    dr_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dr Name'}))
    mob_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_join = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    salary = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Doctor
        fields = '__all__'
        widgets={
            'speciality':forms.Select(attrs={'class':'form-select'}),
            'gender':forms.Select(attrs={'class':'form-select'}),
        }
    
class Patientform(forms.ModelForm):
    class Meta:
        model=PatientAppo
        exclude=['status','created_by']
        widgets={
            'patient_name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-select'}),
            'patient_mob': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'date_appo':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'doctor':forms.Select(attrs={'class':'form-select'}),

        }    

class Admitform(forms.ModelForm):
    class Meta:
        model = Admit
        fields = "__all__"
        widgets={
            # 'patient': forms.TextInput(attrs={'class':'form-control'}),
            'room_no': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-select'}),
            'contact_no': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'admit_date':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'discharge_date':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'deposite_fee':forms.TextInput(attrs={'class':'form-select'}),
        }

class Contactusform(forms.ModelForm):
    cname=forms.CharField(label="Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}))
    cmob = forms.CharField(label="Mobile no.",widget=forms.TextInput(attrs={'class':'form-control'}))
    cdate = forms.CharField(label="Date (choose todays date)",widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    cemail = forms.CharField(label="Email id",widget=forms.TextInput(attrs={'class':'form-control'}))
    cmsg = forms.CharField(label="Message",widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Contactus
        fields = "__all__"
        # widgets={
        #     'cname': forms.TextInput(attrs={'class':'form-control'}),
        #     'cmob': forms.TextInput(attrs={'class':'form-control'}),
        #     'cdate':forms.TextInput(attrs={'class':'form-control','type':'date'}),
        #     'cemail':forms.EmailInput(attrs={'class':'form-select'}),
        #     'cmsg': forms.TextInput(attrs={'class':'form-control'}),
        # }