from django import forms

from library.models import Book, Genre, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'published_year', 'genre', 'ISBN']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']