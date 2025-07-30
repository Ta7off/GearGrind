from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    username = models.CharField(
        max_length=20, unique=True
    )
    is_dealership = models.BooleanField(
        default=False
    )
    profile_image = models.ImageField(
        upload_to='profile_pictures/ ',
        default='profile_pictures/default.png',
        blank=True,
        null=True
    )
    bio = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username