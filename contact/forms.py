from django import forms
from .models import ContactMsg

class ContactMsg(forms.ModelForm):
    class Meta:
        model = ContactMsg
        fields = ['msg_author', 'msg_email', 'msg_message']