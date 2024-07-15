from django import forms

from library.models import Book


class BookForm(forms.Form):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year', 'genre', 'ISBN']