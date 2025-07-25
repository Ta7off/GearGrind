from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# class ChatRoom(models.Model):
#     users = models.ManyToManyField(User)
#     sale = models.ForeignKey(
#         Sale,
#         on_delete=models.SET_NULL,                    #TODO FIX THIS SHIT MAN IDK
#         null=True, blank=True
#     )
#
#     def __str__(self):
#         return f'ChatRoom {self.id}'

# class ChatMessage(models.Model):
#     room = models.ForeignKey(
#         ChatRoom,
#         on_delete=models.CASCADE,
#         related_name='messages'
#     )
#     sender = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     ) # (hidden)
#     message = models.TextField()
#     timestamp = models.DateTimeField(
#         auto_now_add=True
#     ) # (hidden)
#
#     def __str__(self):
#         return f'Message from {self.sender.username} in room {self.room.id}'
