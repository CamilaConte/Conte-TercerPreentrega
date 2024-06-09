from django import forms


class FormCreateDentist(forms.Form):
    tuition = forms.IntegerField()
    name = forms.CharField(max_length=20)