"""
URL configuration for clientes_banco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sistema import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'clientes', views.DadosPessoaisViewSet, basename='clientes')
router.register(r'clientes-completo', views.ClienteCompletoViewSet, basename='clientes-completo')
router.register(r'bancos', views.BancoViewSet, basename='bancos')
router.register(r'contatos', views.ContatoViewSet, basename='contatos')
router.register(r'dados-financeiros', views.DadosFinanceirosViewSet, basename='dados-financeiros')
router.register(r'contas-bancarias', views.ContaBancariaViewSet, basename='contas-bancarias')
router.register(r'cartoes', views.CartaoViewSet, basename='cartoes')
router.register(r'investimentos', views.InvestimentosViewSet, basename='investimentos')
router.register(r'usuarios', views.UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("refresh/token/", TokenRefreshView.as_view()),
    # Rota que gera o arquivo de esquema (YAML/JSON)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Rota do Swagger UI (Interface Interativa)
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Rota do Redoc (visualização mais limpa)
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
