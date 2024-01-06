
from django.contrib import admin
from django.urls import include, path
from .views import HomeView, UserProfileView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),    
    path('', HomeView.as_view(), name='home'),
    path('cadastro-animais/', include('cadastro_animais.urls')),
    path('movimentacao_animais/', include('movimentacao_animais.urls')),
    path('saude_medicamentos/', include('saude_medicamentos.urls')),
    path('reproducao/', include('reproducao.urls')),
    path('pesagem/', include('pesagem.urls')),
    path('genealogia/', include('genealogia.urls')),
    path('custo/', include('custo.urls')),
    path('controle_ambiental/', include('controle_ambiental.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)