from django.urls import path
from .views import home, lista_funcoes, funcao_novo, funcao_update, funcao_search, funcao_delete

urlpatterns = [
    path('home', home, name='home'),
    path('lista_funcoes', lista_funcoes, name='lista_funcoes'),
    path('funcao_novo', funcao_novo, name='funcao_novo'),
    path('funcao_update/<int:id>', funcao_update , name='funcao_update'), 
    path('funcao_search', funcao_search , name='funcao_search'), 
    path('funcao_delete/<int:id>', funcao_delete , name='funcao_delete'), 
]
