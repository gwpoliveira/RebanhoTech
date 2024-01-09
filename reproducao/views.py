from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Reproducao
from .forms import ReproducaoForm
from django.urls import reverse_lazy

class ReproducaoListView(LoginRequiredMixin, ListView):
    model = Reproducao
    template_name = 'reproducao/reproducao_list.html'
    paginate_by=10

class ReproducaoCreateView(LoginRequiredMixin, CreateView):
    model = Reproducao
    template_name = 'reproducao/reproducao_form.html'
    form_class = ReproducaoForm
    success_url = reverse_lazy('reproducao-list')

class ReproducaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Reproducao
    template_name = 'reproducao/reproducao_form.html'
    form_class = ReproducaoForm
    success_url = reverse_lazy('reproducao-list')

class ReproducaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Reproducao
    template_name = 'reproducao/reproducao_confirm_delete.html'
    success_url = reverse_lazy('reproducao-list')
