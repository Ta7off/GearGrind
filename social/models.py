from django.db import models

from accounts.models import UserProfile
from cars.models import Car


class Post(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    images = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_listing = models.BooleanField(default=False)

    likes = models.ManyToManyField(UserProfile, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(UserProfile, related_name='disliked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)