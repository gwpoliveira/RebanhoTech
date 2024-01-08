from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Custo
from .forms import CustoForm

class CustoListView(LoginRequiredMixin,ListView):
    model = Custo
    template_name = 'custo/custo_list.html'
    paginate_by = 10

class CustoCreateView(LoginRequiredMixin,CreateView):
    model = Custo
    template_name = 'custo/custo_form.html'
    form_class = CustoForm
    success_url = reverse_lazy('custo-list')

class CustoUpdateView(LoginRequiredMixin,UpdateView):
    model = Custo
    template_name = 'custo/custo_form.html'
    form_class = CustoForm
    success_url = reverse_lazy('custo-list')

class CustoDeleteView(LoginRequiredMixin,DeleteView):
    model = Custo
    template_name = 'custo/custo_confirm_delete.html'
    success_url = reverse_lazy('custo-list')

