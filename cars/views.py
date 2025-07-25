from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from datetime import timedelta

from bidding.models import Transaction
from cars.forms import CarCreateForm, CarUpdateForm
from cars.models import Car
from social.models import Post


# Create your views here.

class CreateCarView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/create_car.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car-detail', kwargs={'pk': self.object.pk})


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/detail_car.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        car = self.object
        posts = Post.objects.filter(car=car, images__isnull=False).exclude(images='').order_by('-created_at')

        context['posts'] = posts
        return context


class CarUpdateView(UserPassesTestMixin, UpdateView):
    model = Car
    form_class = CarUpdateForm
    template_name = 'cars/edit_car.html'
    success_url = reverse_lazy('car-details')

    def get_object(self, queryset=None):
        return get_object_or_404(Car, pk=self.kwargs['pk'])

    def test_func(self):
        return self.get_object().owner == self.request.user

    def get_success_url(self):
        return reverse('car-detail', kwargs={'pk': self.object.pk})



class CarDeleteView(UserPassesTestMixin, DeleteView):
    model = Car
    template_name = 'cars/delete_car.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Car, pk=self.kwargs['pk'])

    def test_func(self):
        return self.get_object().owner == self.request.user

    def get_success_url(self):
        return reverse('user-details', kwargs={'pk': self.request.user.pk})

@login_required
def start_auction(request, car_id):
    car = get_object_or_404(Car, id=car_id, owner=request.user)

    car.is_listed = True
    car.save()

    return redirect(reverse('car-detail', kwargs={'pk': car.id}))

@login_required
def end_auction(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if car.owner != request.user:
        return HttpResponseForbidden("You're not allowed to end this auction.")

    if not car.is_listed:
        return HttpResponseForbidden("This car is not currently up for auction.")

    highest_bid = car.bids.order_by('-amount').first()

    if highest_bid:
        Transaction.objects.create(
            car=car,
            seller=request.user,
            buyer=highest_bid.bidder,
            final_price=highest_bid.amount
        )
        car.owner = highest_bid.bidder

    car.is_listed = False
    car.save()

    return redirect(reverse('car-detail', kwargs={'pk': car.id}))

@login_required
def cancel_auction(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.is_listed = False
    car.save()

    return redirect(reverse('car-detail', kwargs={'pk': car.id}))
