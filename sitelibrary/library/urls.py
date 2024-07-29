from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('authors/', views.authors, name='authors'),
    path('genres/', views.genres, name='genres'),
    path('genres/<int:id>', views.genre_by_id, name='genre_by_id'),
    path('login/', views.log_in, name='log_in'),
    path('books/<int:id>/', views.book_by_id, name='book_by_id'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/update/<int:id>', views.update_book, name='update_book'),
    path('books/delete/<int:id>', views.delete_book, name='delete_book'),
    path('genres/create/', views.create_genre, name='create_genre'),
    path('genres/update/<int:id>', views.update_genre, name='update_genre'),
    path('genres/delete/<int:id>', views.delete_genre, name='delete_genre'),
]