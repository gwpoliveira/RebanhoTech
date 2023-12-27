from django.urls import path
from .views import CustoListView, CustoCreateView, CustoUpdateView, CustoDeleteView

urlpatterns = [
    path('custo/', CustoListView.as_view(), name='custo-list'),
    path('custo/novo/', CustoCreateView.as_view(), name='custo-create'),
    path('custo/<int:pk>/update/', CustoUpdateView.as_view(), name='custo-update'),
    path('custo/<int:pk>/delete/', CustoDeleteView.as_view(), name='custo-delete'),
]
