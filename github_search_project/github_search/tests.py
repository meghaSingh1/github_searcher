from django.test import TestCase
from django.core.cache import cache
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import SearchAPI, ClearCacheAPI

class SearchAPITestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    
    def test_search_api(self):
        request = self.factory.post('/github_search/api/search', {'search_type': 'users', 'search_text': 'JohnDoe'})
        view = SearchAPI.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ClearCacheAPITestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    
    def test_clear_cache_api(self):
        request = self.factory.post('/github_search/api/clear-cache')
        view = ClearCacheAPI.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNone(cache.get('test_key'))
