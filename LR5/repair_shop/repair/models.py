from django.db import models
from users.models import User


class Request(models.Model):
    STATUSES = [
        ('В ожидании', 'В ожидании'),
        ('Выполнено', 'Выполнена'),
        ('Отклонено', 'Отклонена'),
    ]

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/media/')
    description = models.TextField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='В ожидании')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title
