from django import forms
from .models import Employee 
class employeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nom', 'email', 'poste','salaire']
        widgets = {
            'nom': forms.TextInput(attrs = {
                'class' : 'input w-full',
                'placeholder' : 'Nom complet'
            }),
            'email': forms.TextInput(attrs = {
                'class' : 'input w-full',
                'placeholder' : 'Email address'
            }),
            'poste': forms.TextInput(attrs = {
                'class' : 'input w-full',
                'placeholder' : 'Poste occupé'
            }),
            'salaire': forms.TextInput(attrs = {
                'class' : 'input w-full',
                'placeholder' : 'Salaire en $'
            }),
            
            
        }