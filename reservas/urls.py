from django.urls import path  # Importa o sistema de rotas do Django
from django.contrib.auth import views as auth_views  # Importa views de autenticação
from . import views  # Importa as views do app

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout

    # Rotas para CRUD de reservas
    path('reservas/nova/', views.criar_reserva, name='criar_reserva'),  # Criar reserva
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),  # Editar reserva
    path('reservas/excluir/<int:id>/', views.excluir_reserva, name='excluir_reserva'),  # Excluir reserva
]