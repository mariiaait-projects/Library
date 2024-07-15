from django.http import Http404
from django.shortcuts import render
from library.models import Book

menu = [{"title": "Home", "URL": "home"},
        {"title": "About", "URL": "about"},
        {"title": "Authors", "URL": "authors"},
        {"title": "Genres", "URL": "genres"},
        {"title": "Create book", "URL": "create_book"},
        {"title": "Log in", "URL": "log_in"}]


# Create your views here.
def index(request):
    context = {"title": "Library", 'books': Book.objects.all()}
    return render(request, 'library/index.html', context=context)


def about(request):
    context = {"title": "About"}
    return render(request, 'library/about.html', context=context)


def authors(request):
    authors_data = Book.objects.values_list("author", flat=True).distinct()
    context = {"title": "Authors", 'authors': authors_data}
    return render(request, 'library/authors.html', context=context)


def genres(request):
    genres = Book.objects.values_list("genre", flat=True)
    context = {"title": "Genres", 'genres': set(genres)}
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


# def genre_by_id(request, IDGenre):
#     books_by_genre = []
#     genre_title = ""
#     for genre in list_genre:
#         if genre["IDGenre"] == IDGenre:
#             genre_title = genre["title"]
#             break
#     for book in books:
#         if genre_title == book["genre"]:
#             books_by_genre.append(book)
#     if books_by_genre:
#         return render(request, 'library/genre_by_id.html', context={"books": books_by_genre, "title": genre_title})
#     raise Http404("Genre not found")
