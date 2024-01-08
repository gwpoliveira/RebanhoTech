# pesagem/views.py

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pesagem
from .forms import PesagemForm
from django.urls import reverse_lazy

class PesagemListView(LoginRequiredMixin,ListView):
    model = Pesagem
    template_name = 'pesagem/pesagem_list.html'
    paginate_by=10

class PesagemCreateView(LoginRequiredMixin,CreateView):
    model = Pesagem
    template_name = 'pesagem/pesagem_form.html'
    form_class = PesagemForm
    success_url = reverse_lazy('pesagem-list')

class PesagemUpdateView(LoginRequiredMixin,UpdateView):
    model = Pesagem
    template_name = 'pesagem/pesagem_form.html'
    form_class = PesagemForm
    success_url = reverse_lazy('pesagem-list')

class PesagemDeleteView(LoginRequiredMixin,DeleteView):
    model = Pesagem
    template_name = 'pesagem/pesagem_confirm_delete.html'
    success_url = reverse_lazy('pesagem-list')
