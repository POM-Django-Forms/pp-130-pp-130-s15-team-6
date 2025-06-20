from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('for_user/<int:user_id>/', views.books_for_user, name='books_for_user'),  # ✅ додано
]
