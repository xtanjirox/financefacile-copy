from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from core import models
from core import tables
from core import filters
from django_select2 import forms as s2forms

from .base import BaseListView, FormViewMixin, BaseDeleteView


class FianceEntryListView(BaseListView):
    model = models.FinanceEntry
    table_class = tables.EntriesTable
    filter_class = filters.FinanceEntryFilter
    get_stats = True
    table_pagination = False
    create_url = reverse_lazy('entry-create')
    segment = 'entries'
    detail = True


class FianceEntryCreateView(CreateView, FormViewMixin):
    model = models.FinanceEntry
    template_name = 'generic/create.html'
    fields = '__all__'
    segment = 'entries'
    success_url = reverse_lazy('entry-list')


class FianceEntryUpdateView(UpdateView, FormViewMixin):
    model = models.FinanceEntry
    template_name = 'generic/detail.html'
    fields = '__all__'
    segment = 'entries'
    success_url = reverse_lazy('entry-list')


class FianceEntryDeleteView(BaseDeleteView):
    model = models.FinanceEntry
    success_url = reverse_lazy('entry-list')


class ChargeListView(BaseListView):
    model = models.FinanceEntry
    table_class = tables.EntriesTable
    filter_class = filters.FinanceEntryFilter
    get_stats = True
    table_pagination = False
    create_url = False
    entry_type = models.EntryType.CHARGE
    segment = 'entries'


class RevenueListView(BaseListView):
    model = models.FinanceEntry
    table_class = tables.EntriesTable
    filter_class = filters.FinanceEntryFilter
    get_stats = True
    table_pagination = False
    create_url = False
    entry_type = models.EntryType.REVENUE
    segment = 'entries'
