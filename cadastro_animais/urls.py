from django.urls import path
from .views import AnimalListView, AnimalCreateView, AnimalUpdateView, AnimalDeleteView

urlpatterns = [
    path('animais/', AnimalListView.as_view(), name='animal-list'),
    path('animais/novo/', AnimalCreateView.as_view(), name='animal-create'),
    path('animais/<int:pk>/editar/', AnimalUpdateView.as_view(), name='animal-update'),
    path('animais/<int:pk>/excluir/', AnimalDeleteView.as_view(), name='animal-delete'),
]