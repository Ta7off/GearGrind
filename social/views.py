from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from social.forms import PostCreateForm, CommentForm
from social.models import Post


# Create your views here.

class CreatePostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # user -> form -> shows only the cars the user has
        return kwargs

class DeletePostView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.get_object().author == self.request.user

from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Post, Comment
from .forms import CommentForm


class DetailPostView(DetailView):
    model = Post
    template_name = 'posts/detail_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = self.object
            new_comment.author = request.user
            new_comment.save()
        return redirect('detail-post', pk=self.object.pk)

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    post.dislikes.remove(user)
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect('detail-post', pk=pk)


@login_required
def dislike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    post.likes.remove(user)
    if user in post.dislikes.all():
        post.dislikes.remove(user)
    else:
        post.dislikes.add(user)

    return redirect('detail-post', pk=pk)
