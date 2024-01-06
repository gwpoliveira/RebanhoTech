# saude_medicamentos/views.py

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import SaudeMedicamento
from .forms import SaudeMedicamentoForm
from django.urls import reverse_lazy

class SaudeMedicamentoListView(LoginRequiredMixin, ListView):
    model = SaudeMedicamento
    template_name = 'saude_medicamentos/saudemedicamento_list.html'
    paginate_by=10

class SaudeMedicamentoCreateView(LoginRequiredMixin, CreateView):
    model = SaudeMedicamento
    template_name = 'saude_medicamentos/saudemedicamento_form.html'
    form_class = SaudeMedicamentoForm
    success_url = reverse_lazy('saudemedicamento-list')

class SaudeMedicamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = SaudeMedicamento
    template_name = 'saude_medicamentos/saudemedicamento_form.html'
    form_class = SaudeMedicamentoForm
    success_url = reverse_lazy('saudemedicamento-list')

class SaudeMedicamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = SaudeMedicamento
    template_name = 'saude_medicamentos/saudemedicamento_confirm_delete.html'
    success_url = reverse_lazy('saudemedicamento-list')
