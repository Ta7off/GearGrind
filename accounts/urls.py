from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views import CreateUserView, UserLoginView, UserDetailView, UserLogoutView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('details/<int:pk>/', UserDetailView.as_view(), name='user-details'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/', UserDeleteView.as_view(), name='user-delete'),
]
