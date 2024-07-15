from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('authors/', views.authors, name='authors'),
    path('genres/', views.genres, name='genres'),
    # path('genres/<int:IDGenre>', views.genre_by_id, name='genre_by_id'),
    path('login/', views.log_in, name='log_in'),
    path('books/<int:id>/', views.book_by_id, name='book_by_id'),
    path('books/create/', views.create_book, name='create_book')
]