from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['remitente', 'destinatario', 'texto']

def clean(self):
        cleaned_data = super().clean()
        remitente = cleaned_data.get('remitente')
        destinatario = cleaned_data.get('destinatario')
        texto = cleaned_data.get('texto')
       
        if not remitente:
            self.add_error('remitente', 'Este campo es obligatorio.')
        if not destinatario:
            self.add_error('destinatario', 'Este campo es obligatorio.')
        if not texto:
            self.add_error('texto', 'Este campo es obligatorio.')  