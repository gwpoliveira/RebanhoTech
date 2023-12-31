# views.py em seu aplicativo de controle_ambiental

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CondicaoAmbiental
from .forms import CondicaoAmbientalForm

class CondicaoAmbientalListView(LoginRequiredMixin,ListView):
    model = CondicaoAmbiental
    template_name = 'controle_ambiental/condicaoambiental_list.html'
    paginate_by = 10

class CondicaoAmbientalCreateView(LoginRequiredMixin,CreateView):
    model = CondicaoAmbiental
    template_name = 'controle_ambiental/condicaoambiental_form.html'
    form_class = CondicaoAmbientalForm
    success_url = reverse_lazy('condicaoambiental-list')

class CondicaoAmbientalUpdateView(LoginRequiredMixin,UpdateView):
    model = CondicaoAmbiental
    template_name = 'controle_ambiental/condicaoambiental_form.html'
    form_class = CondicaoAmbientalForm
    success_url = reverse_lazy('condicaoambiental-list')

class CondicaoAmbientalDeleteView(LoginRequiredMixin,DeleteView):
    model = CondicaoAmbiental
    template_name = 'controle_ambiental/condicaoambiental_confirm_delete.html'
    success_url = reverse_lazy('condicaoambiental-list')

