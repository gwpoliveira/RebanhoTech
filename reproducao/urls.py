# reproducao/urls.py

from django.urls import path
from .views import (
    ReproducaoListView,
    ReproducaoCreateView,
    ReproducaoUpdateView,
    ReproducaoDeleteView
)

urlpatterns = [
    path('reproducao/', ReproducaoListView.as_view(), name='reproducao-list'),
    path('reproducao/novo/', ReproducaoCreateView.as_view(), name='reproducao-create'),
    path('reproducao/<int:pk>/editar/', ReproducaoUpdateView.as_view(), name='reproducao-update'),
    path('reproducao/<int:pk>/excluir/', ReproducaoDeleteView.as_view(), name='reproducao-delete'),
]
