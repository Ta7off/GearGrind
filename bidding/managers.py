from django.db import models

class TransactionManager(models.Manager):
    def for_user(self, user):
        return self.filter(models.Q(buyer=user) | models.Q(seller=user))