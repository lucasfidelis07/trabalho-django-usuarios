from django.contrib import admin
from django.urls import path
from posts.views import listar_usuarios, detalhe_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', listar_usuarios),
    path('usuarios/<int:id>/', detalhe_usuario)
]
