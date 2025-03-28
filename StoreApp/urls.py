from StoreApp import views
from django.urls import path


urlpatterns = [
    path('', views.index, name= 'index'),
    path('produtos/', views.produto_lista, name='produto_lista'),
    path('produtos/<int:id>', views.produto_lista_por_id, name='produto_lista_por_id'),
    path('produto/<int:id>', views.produto_detalhe, name='produto_detalhe'),
    path('institucional/', views.sobre_empresa, name='sobre_empresa'), 
    path('contato', views.contato, name='contato'),
    path('cadastro/', views.cadastro, name='cadastro')

]