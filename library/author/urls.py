from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('', views.authors_list, name='authors-list'),                     
    path('create/', views.author_create, name='author-create'),           
    path('<int:author_id>/edit/', views.author_edit, name='author-edit'), 
    path('delete/<int:author_id>/', views.author_delete, name='author-delete'), 
]
