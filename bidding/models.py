from django.db import models

from accounts.models import UserProfile
from bidding.managers import TransactionManager
from cars.models import Car


# Create your models here.

class Bid(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='bids'
    )
    bidder = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    timestamp = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.bidder.username} bid {self.amount} BGN on {self.car}'

class Transaction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    seller = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='sales'
    )

    buyer = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='purchases'
    )

    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    completed_at = models.DateTimeField(auto_now_add=True)

    objects = TransactionManager()

    def __str__(self):
        return f'{self.car} for {self.final_price} BGN between {self.seller} and {self.buyer}'
