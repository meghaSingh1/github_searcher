from django.urls import path
from .views import SearchAPI, ClearCacheAPI

urlpatterns = [
    path('api/search', SearchAPI.as_view(), name='search'),
    path('api/clear-cache', ClearCacheAPI.as_view(), name='clear_cache'),
]
