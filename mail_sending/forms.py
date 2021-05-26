from django import forms
from .models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email']
        widgets = {'email': forms.EmailInput(
            attrs={'style': "outline: none; border: none; padding-top: 0px;padding-bottom: 0px;width: 100%;height: 100%;background-color: #DEECED;font-family: Lora, serif;padding-left: 23px;border:none", 'class': '"border-0"', 'placeholder':"E-mail" }
        )}


class SendMailForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    message = forms.CharField(widget=forms.Textarea,required=False)