from django import forms
from .models import ContactMe

class ContactMeForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email", required=False)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ('name', 'email', 'message')
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})

        }