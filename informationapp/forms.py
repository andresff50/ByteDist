from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control required'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control required'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control required'}))