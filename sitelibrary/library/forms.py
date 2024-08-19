from django import forms

from library.models import Book, Genre, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_year', 'genre', 'ISBN']
        authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple,
                                                required=True)
        genre = forms.ModelChoiceField(queryset=Genre.objects.all(), widget=forms.Select, required=True)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book name', "class": "form-control"}),
            'published_year': forms.NumberInput(attrs={'placeholder': 'Enter book\'s year'}),
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