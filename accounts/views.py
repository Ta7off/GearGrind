from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import UserCreateForm, UserEditForm
from accounts.models import UserProfile


# Create your views here.

class CreateUserView(CreateView):
    model = UserProfile
    form_class = UserCreateForm
    template_name = 'accounts/register_user.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        if not user.profile_image:
            user.profile_image = 'https://static.vecteezy.com/system/resources/previews/020/911/740/non_2x/user-profile-icon-profile-avatar-user-icon-male-icon-face-icon-profile-icon-free-png.png'
        user.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')


class UserDetailView(DetailView):
    model = UserProfile
    template_name = 'accounts/user-details.html'
    context_object_name = 'profile'


class UserLogoutView(LogoutView):
    template_name = 'accounts/logged_out_screen.html'


class UserUpdateView(UpdateView, UserPassesTestMixin):
    model = UserProfile
    form_class = UserEditForm
    template_name = 'accounts/edit_user.html'

    def get_object(self, queryset=None):
        return self.request.user

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('user-details', kwargs={'pk': self.object.pk})


class UserDeleteView(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('home')
    template_name = 'accounts/delete-user.html'

    def get_object(self, queryset=None):
        return self.request.user
