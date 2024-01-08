from django.urls import path
from .views import GenealogiaListView, GenealogiaCreateView, GenealogiaUpdateView, GenealogiaDeleteView

urlpatterns = [
    path('list/', GenealogiaListView.as_view(), name='genealogia-list'),
    path('create/', GenealogiaCreateView.as_view(), name='genealogia-create'),
    path('<int:pk>/update/', GenealogiaUpdateView.as_view(), name='genealogia-update'),
    path('<int:pk>/delete/', GenealogiaDeleteView.as_view(), name='genealogia-delete'),
    
]
