from django import forms


class EmployeerForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.CharField(max_length=120)
    addres = forms.CharField(max_length=20)
