# movimentacao_animais/urls.py

from django.urls import path
from .views import (
    MovimentacaoAnimalListView,
    MovimentacaoAnimalCreateView,
    MovimentacaoAnimalUpdateView,
    MovimentacaoAnimalDeleteView
)

urlpatterns = [
    path('movimentacoes/', MovimentacaoAnimalListView.as_view(), name='movimentacaoanimal-list'),
    path('movimentacoes/nova/', MovimentacaoAnimalCreateView.as_view(), name='movimentacaoanimal-create'),
    path('movimentacoes/<int:pk>/editar/', MovimentacaoAnimalUpdateView.as_view(), name='movimentacaoanimal-update'),
    path('movimentacoes/<int:pk>/excluir/', MovimentacaoAnimalDeleteView.as_view(), name='movimentacaoanimal-delete'),
]
