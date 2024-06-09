from django.shortcuts import redirect, render
from base.models import Dentist
from base.forms import FormCreateDentist

def home(request):
    return render(request, 'index.html')

def save_dentist(request):
    form = FormCreateDentist()
    
    if request.method == 'POST':
        form = FormCreateDentist(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            dentist = Dentist(tuition=data.get('tuition'), name=data.get('name'))
            dentist.save()
            return redirect('list_dentists')
            
    return render(request, 'create_dentist.html', {'form': form})

def list_dentist(request):
    dentists = Dentist.objects.all()
    return render(request, 'list_dentist.html', {'dentists': dentists})