from django.db import models

from users.forms import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} at {self.created_at}, rating: {self.rating}'


class PromoCode(models.Model):
    CODE_TYPES = (
        ('CASHBACK', 'Кэшбек 10%'),
        ('DISCOUNT', '-200 на первую заявку'),
    )

    code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=CODE_TYPES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class UsedPromoCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE)
    used_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.promo_code.code}"
