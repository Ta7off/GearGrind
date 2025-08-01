from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    username = models.CharField(
        max_length=20, unique=True
    )
    profile_image = models.URLField(
        blank=True,
        null=True,
        default='https://static.vecteezy.com/system/resources/previews/020/911/740/non_2x/user-profile-icon-profile-avatar-user-icon-male-icon-face-icon-profile-icon-free-png.png'
    )
    bio = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username