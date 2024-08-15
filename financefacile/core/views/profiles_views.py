from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from core import tables, filters
from account.models import Account

from .base import BaseListView, FormViewMixin, BaseDeleteView
from django_select2 import forms as s2forms


class AccountListView(BaseListView):
    model = Account
    table_class = tables.AccountTable
    filter_class = filters.EntryCategoryFilter
    get_stats = False
    table_pagination = False
    create_url = reverse_lazy('category-create')
    segment = 'categories'

