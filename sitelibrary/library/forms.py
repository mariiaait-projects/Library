from django import forms

from library.models import Book, Genre


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year', 'genre', 'ISBN']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']
