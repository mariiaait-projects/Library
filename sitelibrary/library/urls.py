from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('authors/', views.authors, name='authors'),
    path('login/', views.log_in, name='log_in'),
    path('books/<int:IDBook>', views.book_by_id, name='book_by_id')
]