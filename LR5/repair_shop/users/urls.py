from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, include, reverse_lazy

from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register', Register.as_view(), name='register'),

    path('password_reset/',
         PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
         ),
         name="password_reset"),

    path('password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name="registration/password_reset_done.html"
         ),
         name="password_reset_done"),

    path('reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html"
         ),
         name="password_reset_confirm"),

    path('password_reset/complete/',
         PasswordResetCompleteView.as_view(
             template_name="registration/password_reset_complete.html"
         ),
         name="password_reset_complete"),]
