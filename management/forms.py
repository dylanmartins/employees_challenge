from django import forms

class CreateEmployeeForm(forms.Form):

    name = forms.CharField(label='Name')
    email = forms.EmailField(label='E-mail')
    department = forms.CharField(label='Department')