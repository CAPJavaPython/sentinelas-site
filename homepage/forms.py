from . import models
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = models.Integrante
        fields = ['birth_date', 'telefone']
        labels = {
            'birth_date': 'Data de Nascimento',
            'telefone': 'Número de Telefone',
        }
        widgets = {
            'birth_date': forms.DateInput(
                format='%d/%m/%Y', 
                attrs={
                    'class': 'form-control', 
                    'type': 'date'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '00 00000-0000',
                    'id': 'telefone',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].required = False
        self.fields['telefone'].required = False