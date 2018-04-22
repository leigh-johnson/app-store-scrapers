from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

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

