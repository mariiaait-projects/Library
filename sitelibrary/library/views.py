from django.http import Http404
from django.shortcuts import render
from library.models import Book


# def get_authors():
#     authors_data = []
#
#     for book in books:
#         author = book["author"]
#         if not any(map(lambda data: data["author"] == author, authors_data)):
#             authors_data.append({"author": book["author"]})
#     return authors_data


menu = [{"title": "Home", "URL": "home"},
        {"title": "About", "URL": "about"},
        {"title": "Authors", "URL": "authors"},
        {"title": "Genres", "URL": "genres"},
        {"title": "Log in", "URL": "log_in"}]

list_genre = [{"IDGenre": 1, "title": "Fiction"},
              {"IDGenre": 2, "title": "Science"},
              {"IDGenre": 3, "title": "Technology"},
              {"IDGenre": 4, "title": "Fantasy"}]

# data = {"books": books,
#         "title": "Library",
#         "authors": get_authors()}


# Create your views here.
def index(request):
    context = {'books': Book.objects.all()}
    return render(request, 'library/index.html', context=context)


def about(request):
    return render(request, 'library/about.html')


def authors(request):
    context = {'authors': Book.objects.values_list("author", flat=True).distinct()}
    return render(request, 'library/authors.html', context=context)


def genres(request):
    return render(request, 'library/genres.html')


def log_in(request):
    return render(request, 'library/log_in.html')


# def book_by_id(request, IDBook):
#     for book in books:
#         if book["IDBook"] == IDBook:
#             return render(request, 'library/book_by_id.html', context=book)
#     raise Http404("Book not found")


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
