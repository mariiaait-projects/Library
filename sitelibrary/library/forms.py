from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from library.models import Book, Genre, Author, CartHeader


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_year', 'genre', 'ISBN']
        authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.SelectMultiple,
                                                required=True)
        genre = forms.ModelChoiceField(queryset=Genre.objects.all(), widget=forms.Select(attrs={'placeholder': 'Enter genre',
                "class": "form-control"}), required=True)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book name', "class": "form-control"}),
            'published_year': forms.NumberInput(attrs={'placeholder': 'Enter book\'s year', "class": "form-control"}),
            'ISBN': forms.TextInput(attrs={'placeholder': 'Enter ISBN-number', "class": "form-control"}),
            'genre': forms.Select(attrs={'placeholder': 'Enter genre', "class": "form-control"}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']
        widgets = {'genre': forms.TextInput(attrs={'placeholder': 'Enter genre', "class": "form-control"})}

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Enter name', "class": "form-control"})}

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter username', "class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', "class": "form-control"}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', "class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter username', "class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', "class": "form-control"}))

class CouponApplyForm(forms.Form):
    class Meta:
        model = CartHeader
        fields = ['coupon']
        widgets = {'coupon': forms.TextInput(attrs={'placeholder': 'Enter coupon', "class": "form-control"})}