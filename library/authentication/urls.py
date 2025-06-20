from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.users_list, name='users-list'),
    path('users/<int:user_id>/', views.user_detail, name='user-detail'),
    path('users/<int:user_id>/books/', views.books_for_user, name='books-for-user'),
]