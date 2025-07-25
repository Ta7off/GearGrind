from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from social.models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'core/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

from django.db.models import Q

def search_results(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'core/search_results.html', {
        'query': query,
        'results': results
    })

