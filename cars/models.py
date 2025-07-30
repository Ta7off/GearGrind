from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Car(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_cars'
    )
    make = models.CharField(
        max_length=50
    )
    model = models.CharField(
        max_length=50
    )
    year = models.PositiveIntegerField()
    description = models.TextField(
        blank=True,
        null=True,
    )
    is_listed = models.BooleanField(
        default=False
    )
    image = models.ImageField(
        upload_to='car_pictures/',
        default='car_pictures/default.png',
    )

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'