from django import forms

class CreateDentist(forms.Form):
    tuition = forms.IntegerField()
    name = forms.CharField(max_length=20)