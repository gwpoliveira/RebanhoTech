# saude_medicamentos/urls.py

from django.urls import path
from .views import (
    SaudeMedicamentoListView,
    SaudeMedicamentoCreateView,
    SaudeMedicamentoUpdateView,
    SaudeMedicamentoDeleteView
)

urlpatterns = [
    path('saude-medicamentos/', SaudeMedicamentoListView.as_view(), name='saudemedicamento-list'),
    path('saude-medicamentos/novo/', SaudeMedicamentoCreateView.as_view(), name='saudemedicamento-create'),
    path('saude-medicamentos/<int:pk>/editar/', SaudeMedicamentoUpdateView.as_view(), name='saudemedicamento-update'),
    path('saude-medicamentos/<int:pk>/excluir/', SaudeMedicamentoDeleteView.as_view(), name='saudemedicamento-delete'),
]
