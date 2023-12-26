from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import AnimalForm
from django.urls import reverse_lazy

class AnimalListView(ListView):
    model = Animal
    template_name = 'cadastro_animais/animal_list.html'
    paginate_by=10

class AnimalCreateView(CreateView):
    model = Animal
    template_name = 'cadastro_animais/animal_form.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animal-list')

class AnimalUpdateView(UpdateView):
    model = Animal
    template_name = 'cadastro_animais/animal_form.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animal-list')

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = 'cadastro_animais/animal_confirm_delete.html'
    success_url = reverse_lazy('animal-list')
