from django.urls import path
from .views import CondicaoAmbientalListView, CondicaoAmbientalCreateView, CondicaoAmbientalUpdateView, CondicaoAmbientalDeleteView

urlpatterns = [
    path('condicoes_ambientais/', CondicaoAmbientalListView.as_view(), name='condicaoambiental-list'),
    path('condicoes_ambientais/nova/', CondicaoAmbientalCreateView.as_view(), name='condicaoambiental-create'),
    path('condicoes_ambientais/<int:pk>/atualizar/', CondicaoAmbientalUpdateView.as_view(), name='condicaoambiental-update'),
    path('condicoes_ambientais/<int:pk>/excluir/', CondicaoAmbientalDeleteView.as_view(), name='condicaoambiental-delete'),
]
