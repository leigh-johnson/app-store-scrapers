# python
import random
# lib
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.views import View
from django.core.cache import cache
from django.urls import reverse
import requests
# app
from .models import Keyword

# Create your views here.


class KeywordListView(LoginRequiredMixin, ListView):
    model = Keyword
    # These next two lines tell the view to index lookups by text
    slug_field = "text"
    slug_url_kwarg = "text"

class KeywordCreateView(LoginRequiredMixin, CreateView):
    model = Keyword
    fields = ['text']
    template_name_suffix = '_create_form'

    def get_success_url(self):
        # if a popularity scrape has been done in the past 24 hours, go straight to detail view
        text = self.kwargs.get('text')
        return reverse('scrapers.keyword_popularity_scrape')


class KeywordPopularyScrapeView(View):

    def get(self, request, *args, **kwargs):

        cookies = cache.get('cookie:app.searchads.apple.com')
        csrf_token = cache.get('csrf_token:app.searchads.apple.com')

        url = 'https://app.searchads.apple.com/cm/api/v1/keywords/recommendation'

        query = {
            'adamId': '1308082090',
            'storefronts': 'US',
            'text': keyword
        }

        headers = {
            'Cookie': cookies,
            'X-XSRF-TOKEN-CM': csrf_token,
            'Host': 'app.searchads.apple.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'apple-request-id': random.randint(1e13, 9e13),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Referer': 'https://app.searchads.apple.com/cm/app/campaign',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        res = request.get(url, params=query, headers=headers)




