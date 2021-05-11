from django import forms
from .models import Deposit


class AddDeposit(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['deposit', 'term', 'rate']