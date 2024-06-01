from datetime import date

import pytz
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    date_of_birth = models.DateField(null=True, blank=True)

    @property
    def age(self):
        if self.date_of_birth:
            return (date.today() - self.date_of_birth).days // 365
        return None
