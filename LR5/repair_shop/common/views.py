from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render

from common.forms import ReviewForm, ApplyPromoCodeForm
from common.models import Review, UsedPromoCode, PromoCode
from repair.models import Request
from users.models import User
import urllib.parse
from sklearn.linear_model import LinearRegression
import numpy as np
import requests


def statistics(request):
    requests = Request.objects.all()
    users = User.objects.filter(request__isnull=False).distinct()

    balances = []
    prices = []

    for user in users:
        user_requests = requests.filter(user=user)
        for req in user_requests:
            balances.append(float(user.balance))
            prices.append(float(req.price))

    X = np.array(balances).reshape(-1, 1)
    y = np.array(prices)

    model = LinearRegression()
    model.fit(X, y)

    x_new = np.linspace(min(balances), max(balances), 100).reshape(-1, 1)
    y_new = model.predict(x_new)

    fig, ax = plt.subplots()
    ax.scatter(balances, prices, color='blue', label='Данные')
    ax.plot(x_new, y_new, color='red', label='Линейная регрессия')
    ax.set_title('Зависимость цены заявки от баланса пользователя')
    ax.set_xlabel('Баланс пользователя')
    ax.set_ylabel('Цена заявки')
    ax.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    return render(request, 'statistics.html', {'data': uri})


def reviews(request):
    if request.method == 'POST':
        if request.user.is_authenticated and not request.user.is_superuser:
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = form.save(commit=False)
                new_review.user = request.user
                new_review.save()
                return redirect('reviews')
        else:
            return render(request, 'reviews.html', {'form': ReviewForm(), 'reviews': Review.objects.all().order_by('-created_at'), 'error': 'Суперпользователям запрещено оставлять отзывы.'})
    else:
        form = ReviewForm()

    all_reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews.html', {'form': form, 'reviews': all_reviews})


def contacts(request):
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


# =apple&from
def news(request):
    url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bdab70b929a249a3bd4420bce79ef432'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    print(data)
    return render(request, 'news.html', context={'articles': articles})


def main_page(request):
    url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bdab70b929a249a3bd4420bce79ef432'
    response = requests.get(url)
    news_data = response.json()
    if news_data['status'] == 'ok' and news_data['totalResults'] > 0:
        article = news_data['articles'][0]  # Первый результат
    else:
        article = None
    return render(request, 'main_page.html', {'article': article})


def faq(request):
    faqs = [
        {
            "question": "Как я могу создать заявку?",
            "answer": "Для создания заявки необходимо зарегистрироваться и войти в систему. Затем перейдите на страницу создания заявки и заполните все необходимые поля."
        },
        {
            "question": "Как я могу пополнить баланс?",
            "answer": "Для пополнения баланса перейдите в личный кабинет и выберите опцию пополнения баланса. Введите сумму и подтвердите действие."
        },
        {
            "question": "Как я могу отредактировать свою заявку?",
            "answer": "Чтобы отредактировать заявку, перейдите в раздел 'Мои заявки', выберите нужную заявку и нажмите кнопку 'Редактировать'. Внесите изменения и сохраните."
        },
        {
            "question": "Что делать, если у меня возникли проблемы с использованием сайта?",
            "answer": "Если у вас возникли проблемы с использованием сайта, свяжитесь с нами по электронной почте qpaljke1@gmail.com или по телефону +375256476968."
        }
    ]
    return render(request, 'faq.html', {'faqs': faqs})


def vacancies(request):
    jobs = [
        {
            "title": "Портной",
            "description": "Ищем опытного портного для работы с ремонтом и пошивом одежды. Требуется опыт работы с различными тканями и швейными машинами.",
            "requirements": "Опыт работы не менее 3 лет, умение работать с клиентами, аккуратность.",
            "salary": "от 2000 руб."
        },
        {
            "title": "Мастер по ремонту обуви",
            "description": "Требуется мастер по ремонту обуви. Обязанности включают починку подошв, замену молний, обработку кожи и другие ремонтные работы.",
            "requirements": "Опыт работы в аналогичной должности не менее 2 лет, внимательность к деталям.",
            "salary": "от 2500 руб."
        },
        {
            "title": "Администратор",
            "description": "Ищем администратора для управления заказами и взаимодействия с клиентами. Требуется уверенный пользователь ПК и опыт работы в сфере обслуживания.",
            "requirements": "Доброжелательность, ответственность, опыт работы в клиентской сфере.",
            "salary": "от 4000 руб."
        }
    ]
    return render(request, 'vacancies.html', {'jobs': jobs})


@login_required
def promo_codes(request):
    if request.method == 'POST':
        form = ApplyPromoCodeForm(request.POST)
        if form.is_valid():
            promo_code_text = form.cleaned_data.get('promo_code')
            try:
                promo_code = PromoCode.objects.get(code=promo_code_text, active=True)
                if UsedPromoCode.objects.filter(user=request.user, promo_code=promo_code).exists():
                    form.add_error('promo_code', 'Этот промокод уже был использован.')
                else:
                    if promo_code.type == 'CASHBACK':
                        first_request = request.user.request_set.first()
                        request.user.balance += first_request / 10
                    elif promo_code.type == 'DISCOUNT':
                        first_request = request.user.request_set.first()
                        if first_request and first_request.price >= promo_code.discount_value:
                            first_request.price -= promo_code.discount_value
                            first_request.save()

                    request.user.save()
                    UsedPromoCode.objects.create(user=request.user, promo_code=promo_code)

                    promo_code.delete()

                    return redirect('promo_codes')
            except PromoCode.DoesNotExist:
                form.add_error('promo_code', 'Недействительный промокод.')
    else:
        form = ApplyPromoCodeForm()

    available_promo_codes = PromoCode.objects.filter(active=True)
    return render(request, 'promo_codes.html', {'form': form, 'available_promo_codes': available_promo_codes})
