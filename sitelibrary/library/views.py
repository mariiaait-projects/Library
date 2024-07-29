from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from library.models import Book, Genre, Author
from library.forms import BookForm

menu = [{"title": "Home", "URL": "home"},
        {"title": "About", "URL": "about"},
        {"title": "Authors", "URL": "authors"},
        {"title": "Genres", "URL": "genres"},
        {"title": "Create book", "URL": "create_book"},
        {"title": "Log in", "URL": "log_in"}]


# Create your views here.
def index(request):
    context = {"title": "Library", 'books': Book.objects.all()}
    print(Book.objects.all())
    return render(request, 'library/index.html', context=context)


def about(request):
    context = {"title": "About"}
    return render(request, 'library/about.html', context=context)


def authors(request):
    authors_data = Author.objects.values_list("name", flat=True)
    context = {"title": "Authors", 'authors': authors_data}
    return render(request, 'library/authors.html', context=context)


def genres(request):
    genres = Genre.objects.all()
    context = {"title": "Genres", 'genres': genres}
    return render(request, 'library/genres.html', context=context)


def log_in(request):
    context = {"title": "Log in"}
    return render(request, 'library/log_in.html', context=context)


def book_by_id(request, id):
    if Book.objects.filter(id=id).exists():
        book = Book.objects.get(id=id)
        context = {'book': book}
        return render(request, 'library/book_by_id.html', context=context)
    raise Http404("Book not found")


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
