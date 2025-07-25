from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from accounts.models import UserProfile
from bidding.forms import CreateBidForm, UpdateBidForm
from bidding.models import Bid, Transaction
from cars.models import Car


# Create your views here.

class CreateBidView(LoginRequiredMixin, CreateView):
    model = Bid
    form_class = CreateBidForm
    template_name = 'bidding/place_bid.html'

    def dispatch(self, request, *args, **kwargs):
        self.car = get_object_or_404(Car, id=self.kwargs['car_id'])

        if self.car.owner == request.user:
            return HttpResponseForbidden('cannot place a bid on your car')
        if not self.car.is_listed:
            return HttpResponseForbidden("This car is not listed for auction.")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        existing_bid = Bid.objects.filter(car=self.car, bidder=self.request.user).first()

        bid = form.save(commit=False)

        if existing_bid:
            bid.pk = existing_bid.pk

        bid.car = self.car
        bid.bidder = self.request.user
        bid.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car-detail', args=[self.car.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = self.car

        context['existing_bid'] = Bid.objects.filter(car=self.car, bidder=self.request.user).first()

        return context

class ListBidView(ListView):
    model = Bid
    template_name = 'bidding/list_bids.html'

    def get_queryset(self):
        return Bid.objects.filter(bidder=self.request.user)

class DeleteBidView(LoginRequiredMixin, DeleteView):
    model = Bid
    template_name = 'bidding/confirm_delete.html'
    success_url = reverse_lazy('list-bid')

    def get_queryset(self):
        return Bid.objects.filter(bidder=self.request.user)

class UpdateBidView(LoginRequiredMixin, UpdateView):
    model = Bid
    form_class = UpdateBidForm
    template_name = 'bidding/update_bid_form.html'
    success_url = reverse_lazy('list-bid')

class TransactionListView(ListView):
    model = Transaction
    template_name = 'bidding/transaction_history.html'
    def get_queryset(self):
        profile_id = self.kwargs.get('profile_id')
        profile = get_object_or_404(UserProfile, id=profile_id)
        return Transaction.objects.filter(Q(seller=profile) | Q(buyer=profile))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = self.kwargs.get('profile_id')
        profile = get_object_or_404(UserProfile, id=profile_id)
        context['profile'] = profile
        return context

