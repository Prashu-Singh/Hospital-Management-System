from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views import View
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages

# Create your views here.

def homee(request):
    return render(request,'home.html')

# Login & logout section
# ---------------------------

def sign_up(request):
    if request.method == 'POST':
        myform = UserCreationForm(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request,"Sign up successfully...")
        else:
            messages.error(request,"Something went wrong...")
        return render (request,'signup.html',{'myform':myform})
    else:
        myform = UserCreationForm()
        return render (request,'signup.html',{'myform':myform})

def log_in(request):
    if request.method == 'POST':
        myform = AuthenticationForm(request=request,data=request.POST)
        if myform.is_valid():    
            uname = myform.cleaned_data['username']
            pasw = myform.cleaned_data['password']

            request.session['uname'] = uname
            user = authenticate(username=uname,password=pasw)
            login(request,user)
            return redirect('home')
        return render (request,'login.html',{'myform':myform})
    else:
        myform = AuthenticationForm()
        return render (request,'login.html',{'myform':myform})


def log_out(request):
    logout(request)
    return redirect('loginuser')





# Doctor section
# -------------------------

def showdrdata(request):
    if request.user.is_superuser:
        data = Doctor.objects.all()
    else:
        data=Doctor.objects.filter(dr_name=request.user)

    if request.method == 'POST':
        if request.POST['dform'] == "searchform":
            drname = request.POST['drname']
            ddata=Doctor.objects.filter(dr_name__startswith = drname)
            return render(request,'showdrdata.html',{"data":ddata})
        
        elif request.POST['dform'] == "dateform":
            date1 = request.POST['date1']
            date2 = request.POST['date2']
            data = Doctor.objects.filter(date_of_join__lte=date2,date_of_join__gte=date1)
            return render(request,'showdrdata.html',{"data":data})
    else:
        return render(request,'showdrdata.html',{'data':data})
    
def add_doctor(request):
    if request.method == 'POST':
        myform = Doctoform(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('drdata')
        return render(request,'add_doctor.html',{'drform':myform})
    else:
        myform = Doctoform()
        return render(request,'add_doctor.html',{'drform':myform})
    
# Doctors detail updation section

def upd_doctor(request,id):
    if request.method == 'POST':
        obj = Doctor.objects.get(id=id)
        myform = Doctoform(request.POST,instance=obj)
        if myform.is_valid():
            myform.save()
            return redirect('drdata')
        return render(request,'updatedr.html',{'drform':myform})
    else:
        obj = Doctor.objects.get(id=id)
        myform = Doctoform(instance=obj)
        return render(request,'updatedr.html',{'drform':myform})
    
# Doctors Detail deletion section

def del_doctor(request,id):
    data = Doctor.objects.get(id = id)
    data.delete()
    return redirect('drdata')




# Appoinment Section
# ----------------------------

def showdappodata(request):
    if request.user.is_superuser:
        data = PatientAppo.objects.all()
    else:
        data=PatientAppo.objects.filter(created_by = request.user)

    if request.method == 'POST':
        if request.POST['sform'] == "searchform":
           pname = request.POST['pname'] 
           pdata = PatientAppo.objects.filter(patient_name__startswith = pname)
           return render(request,'showappoinment.html',{"data":pdata})
        
        elif request.POST['sform'] == "dateform":
            date1 = request.POST['date1']
            date2 = request.POST['date2']
            data = PatientAppo.objects.filter(date_appo__lte=date2,date_appo__gte=date1)
            return render(request,'showappoinment.html',{"data":data})
    else:
        return render(request,'showappoinment.html',{'data':data})
       
def add_appoinment(request):
    if request.method == 'POST':
        patform = Patientform(request.POST)
        if patform.is_valid():
            created_by = request.user
            patient_name = patform.cleaned_data['patient_name']
            age = patform.cleaned_data['age']
            patient_mob = patform.cleaned_data['patient_mob']
            gender = patform.cleaned_data['gender']
            doctor1 = patform.cleaned_data['doctor']
            print(doctor1)
            doctor = Doctor.objects.get(dr_name=doctor1)
            address = patform.cleaned_data['address']
            date_appo = patform.cleaned_data['date_appo']

            obj = PatientAppo(created_by=created_by,patient_name=patient_name,age=age,patient_mob=patient_mob,gender=gender,address=address,date_appo=date_appo,doctor=doctor)
            obj.save()
            return redirect('appodata')
        return render(request,'add_appoinment.html',{'patform':patform})
    
    else:
        patform= Patientform()
        return render(request,'add_appoinment.html',{'patform':patform})

# Appoinment updation section

def upd_appoinment(request,id):
    if request.method == 'POST':
        obj = PatientAppo.objects.get(id=id)
        patform = Patientform(request.POST,instance=obj)
        if patform.is_valid():
            patform.save()
            return redirect('appodata')
        return render(request,'updateappoinmet.html',{'patform':patform})
    else:
        obj = PatientAppo.objects.get(id=id)
        patform = Patientform(instance=obj)
        return render(request,'updateappoinment.html',{'patform':patform})
    
# Appoinment Deletion Section

def del_appoinment(request,id):
    data = PatientAppo.objects.get(id = id)
    data.delete()
    return redirect('appodata')

# Admited Patients Section
# ---------------------------------

def showdadmited_data(request):
    if request.user.is_superuser:
        data = Admit.objects.all()
    else:
        data=Admit.objects.filter(created_by = request.user)

    if request.method == 'POST':
        date1 = request.POST['date1']
        date2 = request.POST['date2']
        data = Admit.objects.filter(admit_date__lte=date2,admit_date__gte=date1)
        return render(request,'showadmitted.html',{"data":data})
    else:
        return render(request,'showadmitted.html',{'data':data})


def addadmitted_patient(request):
    if request.method == 'POST':
        apform = Admitform(request.POST)
        if apform.is_valid():
            apform.save()
            return redirect('admitdata')
        return render(request,'add_admittedpatient.html',{'apform':apform})
    else:
        apform = Admitform()
        return render(request,'add_admittedpatient.html',{'apform':apform})
    
    
def upd_admit(request,id):
    if request.method == 'POST':
        obj = Admit.objects.get(id=id)
        apform = Admitform(request.POST,instance=obj)
        if apform.is_valid():
            apform.save()
            return redirect('admitdata')
        return render(request,'updateadmit.html',{'apform':apform})
    else:
        obj = Admit.objects.get(id=id)
        apform = Admitform(instance=obj)
        return render(request,'updateadmit.html',{'apform':apform})
    
def del_admit(request,id):
    data = Admit.objects.get(id = id)
    data.delete()
    return redirect('admitdata')



# Appoinmnet approval/ rejection section
# --------------------------------------------


def approve(request,id):
    obj = PatientAppo.objects.get(id = id) 
    obj.status = "Approve"
    obj.save()
    return redirect("appodata")

def reject(request,id):
    obj = PatientAppo.objects.get(id = id) 
    obj.status = "Reject"
    obj.save()
    return redirect("appodata")


# Contact us Section
# --------------------------

def contactus(request):
    if request.method == 'POST':
        cform = Contactusform(request.POST)
        if cform.is_valid():
            cform.save()
            return redirect('contactus')
        return render(request,'contact.html',{'cform':cform})
    else:
        cform = Contactusform()
        return render(request,'contact.html',{'cform':cform})
    

def showcontactlist(request):
    data = Contactus.objects.all()
    if request.method == 'POST':
        date1 = request.POST['date1']
        date2 = request.POST['date2']
        data = Contactus.objects.filter(cdate__lte=date2,cdate__gte=date1)
        return render(request,'contactlist.html',{"data":data})
    else:
        return render(request,'contactlist.html',{'data':data})
    

def del_contact(request,id):
    data = Contactus.objects.get(id = id)
    data.delete()
    return redirect('contactlist')