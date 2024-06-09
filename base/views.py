from django.shortcuts import redirect, render
from django.http import HttpResponse
from base.models import Dentist, Patient
from base.forms import FormCreateDentist, FormCreatePatient

def home(request):
    return render(request, 'index.html')

def save_dentist(request):
    form = FormCreateDentist()
    error = ''
    
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            dentist = Dentist(tuition=data.get('tuition'), name=data.get('name'))
            dentist.save()
            return redirect('list_dentist')
        else:
            error = 'Form data is invalid. Please try again.'
            
    return render(request, 'create_dentist.html', {'form': form, 'error': error})

def save_patient(request):
    form = FormCreatePatient()
    error = ''
    
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            patient = Patient(name=data.get('name'), age=data.get('age'))
            patient.save()
            return redirect('list_patient')
        else:
            error = 'Form data is invalid. Please try again.'

    return render(request, 'create_patient.html', {'form': form, 'error': error})

def list_dentist(request):
    dentists = Dentist.objects.all()
    return render(request, 'list_dentist.html', {'dentists': dentists})

def list_patient(request):
    patients = Patient.objects.all()
    return render(request, 'list_patient.html', {'patients': patients})