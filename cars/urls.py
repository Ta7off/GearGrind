from django.urls import path
from django.views.generic import DetailView, UpdateView

from cars.views import CreateCarView, CarDetailView, CarUpdateView, CarDeleteView, start_auction, end_auction, \
    cancel_auction

urlpatterns = [
    path('create/', CreateCarView.as_view(), name='car-create'),
    path('detail/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('edit/<int:pk>/', CarUpdateView.as_view(), name='car-edit'),
    path('delete/<int:pk>/', CarDeleteView.as_view(), name='car-delete'),
    path('car/<int:car_id>/start-auction/', start_auction, name='start-auction'),
    path('car/<int:car_id>/end-auction/', end_auction, name='end-auction'),
    path('car/<int:car_id>/cancel-auction/', cancel_auction, name='cancel-auction'),

]
