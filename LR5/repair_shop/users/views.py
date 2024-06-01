from datetime import timezone, datetime

import pytz
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from users.forms import BalanceForm
from users.forms import UsrCreationForm, PasswordResetForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UsrCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UsrCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


@login_required
def add_balance(request):
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            request.user.balance += amount
            request.user.save()
            messages.success(request, f'Ваш баланс успешно пополнен на {amount} рублей.')
            return redirect('home')  # перенаправление на страницу профиля
    else:
        form = BalanceForm()
    return render(request, 'add_balance.html', {'form': form, 'balance': request.user.balance})


def profile(request):
    if request.user.is_authenticated:
        date = datetime.now(timezone.utc).astimezone()
        return render(request, 'home.html', {'balance': request.user.balance, 'date': date})
    return render(request, 'home.html')
