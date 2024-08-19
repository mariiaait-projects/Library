from django import forms

from library.models import Book, Genre, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_year', 'genre', 'ISBN']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book name'}),
            'authors': forms.MultipleChoiceField(queryset=Author.objects.all()),
            'published_year': forms.NumberInput(attrs={'placeholder': 'Enter book\'s year'}),
            'genre': forms.Select(attrs={}),
            'ISBN': forms.TextInput(attrs={'placeholder': 'Enter ISBN number'})
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']