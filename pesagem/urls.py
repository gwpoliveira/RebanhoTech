# pesagem/urls.py

from django.urls import path
from .views import (
    PesagemListView,
    PesagemCreateView,
    PesagemUpdateView,
    PesagemDeleteView
)

urlpatterns = [
    path('pesagem/', PesagemListView.as_view(), name='pesagem-list'),
    path('pesagem/novo/', PesagemCreateView.as_view(), name='pesagem-create'),
    path('pesagem/<int:pk>/editar/', PesagemUpdateView.as_view(), name='pesagem-update'),
    path('pesagem/<int:pk>/excluir/', PesagemDeleteView.as_view(), name='pesagem-delete'),
]
