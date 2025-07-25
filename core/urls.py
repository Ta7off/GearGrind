from django.urls import path

from core import views
from core.views import HomePageView, search_results

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', search_results, name='search-results'),

]
