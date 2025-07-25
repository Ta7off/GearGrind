from django.urls import path

from bidding.views import CreateBidView, ListBidView, DeleteBidView, UpdateBidView, TransactionListView

urlpatterns = [
    path('create/<int:car_id>/', CreateBidView.as_view(), name='place-bid'),
    path("list/", ListBidView.as_view(), name='list-bid'),
    path('delete/<int:pk>/', DeleteBidView.as_view(), name='delete-bid'),
    path('update/<int:pk>/', UpdateBidView.as_view(), name='update-bid'),
    path('transactions/<int:profile_id>/', TransactionListView.as_view(), name='transaction_history')

]