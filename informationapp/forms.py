from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre y apellidos o el nombre de tu empresa', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control required'}))
    email = forms.EmailField(label='Correo electronico', widget=forms.EmailInput(attrs={'class': 'form-control required'}))
    subject = forms.CharField(label='Motivo por el cual nos contactas', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control required'}))
    message = forms.CharField(label='Resume tu historia', widget=forms.Textarea(attrs={'class': 'form-control required'}))