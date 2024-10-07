from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:id>/', views.author_by_id, name='author_by_id'),
    path('genres/', views.genres, name='genres'),
    path('genres/<int:id>/', views.genre_by_id, name='genre_by_id'),
    path('books/<int:id>/', views.book_by_id, name='book_by_id'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/update/<int:id>/', views.update_book, name='update_book'),
    path('books/delete/<int:id>/', views.delete_book, name='delete_book'),
    path('genres/create/', views.create_genre, name='create_genre'),
    path('genres/update/<int:id>/', views.update_genre, name='update_genre'),
    path('genres/delete/<int:id>/', views.delete_genre, name='delete_genre'),
    path('authors/create/', views.create_author, name='create_author'),
    path('authors/update/<int:id>/', views.update_author, name='update_author'),
    path('authors/delete/<int:id>/', views.delete_author, name='delete_author'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('books/buy/<int:id>', views.buy_book, name='buy_book'),
    path('cart/', views.get_cart, name='cart'),
    path('cart/delete/<int:id>', views.delete_product_from_cart, name='delete_product_from_cart'),
    path('cart/apply-coupon/', views.apply_coupon, name='apply_coupon'),
    path('cart/delete-coupon/', views.delete_coupon, name='delete_coupon'),
    path('search/', views.search_book, name='search_book'),
    path('filter-books/', views.filter_books, name='filter_books')
]