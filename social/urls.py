from django.urls import path

from social.views import CreatePostView, DeletePostView, DetailPostView, like_post, dislike_post

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('detail/<int:pk>', DetailPostView.as_view(), name='detail-post'),
    path('like/<int:pk>', like_post, name='like-post'),
    path('dislike/<int:pk>', dislike_post, name='dislike-post'),
]
