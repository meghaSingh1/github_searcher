import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from requests.exceptions import RequestException
from django.views.generic import View
from django.core.cache import cache
from .models import SearchCache
from cachetools import cached, LRUCache


class SearchAPI(APIView):

    def get_github_data(self, search_type, search_text):
        try:
            cache_key = f'{search_type}_{search_text}'
            cached_data = cache.get(cache_key)

            if cached_data is not None:
                return cached_data
            
            github_api_url = f'https://api.github.com/search/{search_type}'
            params = {'q': search_text}
            response = requests.get(github_api_url, params=params)
            response.raise_for_status() 
            if response.status_code == 200:
                data_from_github = response.json()
                # Caching the data for 2 hours
                cache.set(cache_key, data_from_github, 60 * 60 * 2)
                
                return data_from_github
            
            return Response({"error": "Failed to fetch data from the GitHub API."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except RequestException as e:
            print(e)
            return Response({"error": "Exception occured while fetching data from the GitHub API."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        # search_type = request.POST.get('search_type')
        # search_text = request.POST.get('search_text')
        search_type = request.data.get('search_type')
        search_text = request.data.get('search_text')
    
        if not search_type or not search_text:
            return Response({"error": "Both 'search_type' and 'search_text' are required."}, status=status.HTTP_400_BAD_REQUEST)

        cached_data = self.get_github_data(search_type, search_text)

        if cached_data:
            data = {
                "search_type": search_type,
                "search_text": search_text,
                "data": cached_data
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response({"error": "Failed to fetch data from the GitHub API."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ClearCacheAPI(APIView):
    def post(self, request):
        cache.clear()
        return Response({"message": "Cache cleared successfully"}, status=status.HTTP_200_OK)
