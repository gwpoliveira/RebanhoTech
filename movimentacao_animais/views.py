# movimentacao_animais/views.py

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import MovimentacaoAnimal
from .forms import MovimentacaoAnimalForm
from django.urls import reverse_lazy

class MovimentacaoAnimalListView(LoginRequiredMixin,ListView):
    model = MovimentacaoAnimal
    template_name = 'movimentacao_animais/movimentacaoanimal_list.html'
    paginate_by=10

class MovimentacaoAnimalCreateView(LoginRequiredMixin,CreateView):
    model = MovimentacaoAnimal
    template_name = 'movimentacao_animais/movimentacaoanimal_form.html'
    form_class = MovimentacaoAnimalForm
    success_url = reverse_lazy('movimentacaoanimal-list')

class MovimentacaoAnimalUpdateView(LoginRequiredMixin,UpdateView):
    model = MovimentacaoAnimal
    template_name = 'movimentacao_animais/movimentacaoanimal_form.html'
    form_class = MovimentacaoAnimalForm
    success_url = reverse_lazy('movimentacaoanimal-list')

class MovimentacaoAnimalDeleteView(LoginRequiredMixin,DeleteView):
    model = MovimentacaoAnimal
    template_name = 'movimentacao_animais/movimentacaoanimal_confirm_delete.html'
    success_url = reverse_lazy('movimentacaoanimal-list')

