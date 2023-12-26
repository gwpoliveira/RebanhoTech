from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Genealogia
from .forms import GenealogiaForm

class GenealogiaListView(ListView):
    model = Genealogia
    template_name = 'genealogia/genealogia_list.html'
    paginate_by = 10

class GenealogiaCreateView(CreateView):
    model = Genealogia
    template_name = 'genealogia/genealogia_form.html'
    form_class = GenealogiaForm
    success_url = reverse_lazy('genealogia-list')

    def form_valid(self, form):
        form.instance.foto_animal = form.instance.identificacao.foto
        return super().form_valid(form)

class GenealogiaUpdateView(UpdateView):
    model = Genealogia
    template_name = 'genealogia/genealogia_form.html'
    form_class = GenealogiaForm
    success_url = reverse_lazy('genealogia-list')

    def form_valid(self, form):
        form.instance.foto_animal = form.instance.identificacao.foto
        return super().form_valid(form)

class GenealogiaDeleteView(DeleteView):
    model = Genealogia
    template_name = 'genealogia/genealogia_confirm_delete.html'
    success_url = reverse_lazy('genealogia-list')
