from django.urls import path
from api_cliente import views

urlpatterns=[

    path('', views.Listar_cliente, name="Clientes"),
    path('detalle/<str:pk>', views.Detalle_cliente, name="Detalles_clientes"),
    path('crear', views.Registro_cli, name="Registar_cleinte"),
    path('actualizar/<str:pk>/', views.Actualizar_cliente, name="Actualizar_cliente"),
    path('eliminar/<str:pk>/', views.Eliminar_cliente, name="Eliminar_cliente"),
]