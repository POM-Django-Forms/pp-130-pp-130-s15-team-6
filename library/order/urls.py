from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.orders_list, name='orders-list'),
    path('create/', views.order_create, name='order-create'),
    path('<int:order_id>/edit/', views.order_edit, name='order-edit'), 
    path('delete/<int:order_id>/', views.order_delete, name='order-delete'),
]
