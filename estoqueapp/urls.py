from django.urls import path
from . import views

app_name = "estoqueapp"

urlpatterns = [
    # /estoqueapp/
    path('rel_perfis/', views.lista, name="lista_perfis"),
    # path('rel_perfis/create', views.create, name="create_perfis"),
    path('rel_perfis/delete/<int:rel_perfis_id>', views.delete, name="delete_perfis"),
    path('rel_perfis/update/<int:rel_perfis_id>', views.update, name="editar_perfis"),
    # path('rel_perfis/<int:rel_perfis_id>', views.read, name="read_perfis"),
]
