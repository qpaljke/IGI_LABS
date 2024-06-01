from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UsrCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    date_of_birth = forms.DateField(
        label=_("Дата рождения"),
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'date_of_birth')

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            age = (date.today() - date_of_birth).days // 365
            if age < 18:
                raise forms.ValidationError("Вам должно быть не менее 18 лет для регистрации.")
        return date_of_birth


class BalanceForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01, label='Сумма пополнения')

