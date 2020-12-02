from django import forms

from . models import Marca

class MarcaForm(forms.ModelForm):
    marca = forms.CharField(label='Marca',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Marca
        fields = ('marca',)