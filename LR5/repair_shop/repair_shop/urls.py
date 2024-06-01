from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import profile, add_balance
from common.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),

    # path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', profile, name='home'),

    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('FAQ/', faq, name='faq'),
    path('contacts/', contacts, name='contacts'),
    path('privacy-policy/', TemplateView.as_view(template_name='privacy_policy.html'), name='privacy_policy'),
    path('vacancies/', vacancies, name='vacancies'),
    path('reviews/', reviews, name='reviews'),
    path('add-balance/', add_balance, name='add_balance'),
    path('statistics/', statistics, name='statistics'),
    # path('add-balance/', TemplateView.as_view(template_name='add_balance.html'), name='add_balance'),

    path('users/', include('users.urls')),

    path('repair/', include('repair.urls')),

    path('promo_codes/', promo_codes, name='promo_codes'),
]
