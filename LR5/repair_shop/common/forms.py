from django import forms

from common.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': '1', 'max': 5}),
        }


class ApplyPromoCodeForm(forms.Form):
    promo_code = forms.CharField(max_length=20, label='Введите промокод')
