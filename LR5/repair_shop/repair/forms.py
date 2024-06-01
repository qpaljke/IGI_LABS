from django import forms
from repair.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'image', 'description', 'price']