from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from library.models import Book, Genre, Author, BookAuthor, Cart
from library.forms import BookForm, GenreForm, AuthorForm

menu = [{"title": "Home", "URL": "home"},
        {"title": "About", "URL": "about"},
        {"title": "Authors", "URL": "authors"},
        {"title": "Genres", "URL": "genres"},
        {"title": "Create book", "URL": "create_book"},
        {"title": "Create genre", "URL": "create_genre"},
        {"title": "Create author", "URL": "create_author"},
        {"title": "Log in", "URL": "log_in"}]


# Create your views here.
def index(request):
    context = {"title": "Library", 'books': Book.objects.all()}
    return render(request, 'library/index.html', context=context)


def about(request):
    context = {"title": "About"}
    return render(request, 'library/about.html', context=context)


def authors(request):
    authors = Author.objects.all()
    context = {"title": "Authors", 'authors': authors}
    return render(request, 'library/authors.html', context=context)


def genres(request):
    genres = Genre.objects.all()
    context = {"title": "Genres", 'genres': genres}
    return render(request, 'library/genres.html', context=context)


def log_in(request):
    context = {"title": "Log in"}
    return render(request, 'library/log_in.html', context=context)


def book_by_id(request, id):
    book = get_object_or_404(Book, id=id)
    authors_ids = BookAuthor.objects.filter(book_id=book.id).values_list('author', flat=True)
    authors = Author.objects.filter(id__in=authors_ids)
    context = {'book': book, 'authors': authors}
    return render(request, 'library/book_by_id.html', context=context)



def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_by_id', id=book.id)
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', context={"form": form})


def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_by_id', id=book.id)
    else:
        form = BookForm(instance=book)
        return render(request, 'library/book_form.html', context={"form": form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home')


def genre_by_id(request, id):
    books = Book.objects.filter(genre_id=id)
    title = Genre.objects.get(id=id)
    context = {"title": title, "books": books}
    return render(request, 'library/genre_by_id.html', context=context)

def create_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genres')
    else:
        form = GenreForm()
    return render(request, 'library/genre_form.html', context={"form": form})

def update_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genres')
    else:
        form = GenreForm(instance=genre)
        return render(request, 'library/genre_form.html', context={"form": form})

def delete_genre(request,id):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    return redirect('genres')

def author_by_id(request, id):
    author = get_object_or_404(Author, id=id)
    books = Book.objects.filter(authors__id=author.id)
    context = {"title": author.name, "books": books}
    print(books)
    return render(request, 'library/author_by_id.html', context=context)
def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'library/author_form.html', context={"form": form})

def update_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm(instance=author)
        return render(request, 'library/author_form.html', context={"form": form})

def delete_author(request,id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('authors')

def buy_book(request, id):
    book = get_object_or_404(Book, id=id)
    cart = Cart.objects.create(book=book)
    return redirect('get_cart')

def get_cart(request):
    purchases = Cart.objects.all()
    total = sum(map(lambda purchase: purchase.book.price * purchase.quantity, purchases))
    return render(request, 'library/cart.html', context={'title': "Cart", 'purchases': purchases, 'total': total})

def delete_product_from_cart(request, id):
    product = get_object_or_404(Cart, id=id)
    product.delete()
    return redirect('get_cart')


