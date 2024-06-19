from django.http import Http404
from django.shortcuts import render

books = [
    {
        "IDBook": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960,
        "genre": "Fiction",
        "ISBN": "978-0-06-112008-4"
    },
    {
        "IDBook": 2,
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949,
        "genre": "Dystopian",
        "ISBN": "978-0-452-28423-4"
    },
    {
        "IDBook": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_year": 1813,
        "genre": "Romance",
        "ISBN": "978-0-19-953556-9"
    },
    {
        "IDBook": 4,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "genre": "Tragedy",
        "ISBN": "978-0-7432-7356-5"
    },
    {
        "IDBook": 5,
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "published_year": 1851,
        "genre": "Adventure",
        "ISBN": "978-0-14-243724-7"
    },
    {
        "IDBook": 6,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "published_year": 1869,
        "genre": "Historical Fiction",
        "ISBN": "978-0-19-923276-5"
    },
    {
        "IDBook": 7,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "published_year": 1951,
        "genre": "Fiction",
        "ISBN": "978-0-316-76948-0"
    },
    {
        "IDBook": 8,
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "published_year": 1954,
        "genre": "Fantasy",
        "ISBN": "978-0-618-00222-8"
    },
    {
        "IDBook": 9,
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "published_year": 1847,
        "genre": "Romance",
        "ISBN": "978-0-14-144114-6"
    },
    {
        "IDBook": 10,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "published_year": 1937,
        "genre": "Fantasy",
        "ISBN": "978-0-618-00221-1"
    }
]


def get_authors():
    authors_data = []

    for book in books:
        author = book["author"]
        if not any(map(lambda data: data["author"] == author, authors_data)):
            authors_data.append({"author": book["author"]})
    return authors_data


menu = [{"title": "Home", "URL": "home"}, {"title": "About", "URL": "about"}, {"title": "Authors", "URL": "authors"},
        {"title": "Genres", "URL": "genres"}, {"title": "Log in", "URL": "log_in"}]

list_genre = [{"id": 1, "title": "Fiction"}, {"id": 2, "title": "Science"}, {"id": 3, "title": "Technology"},
              {"id": 4, "title": "Fantasy"}]

data = {"books": books, "title": "Library", "menu": menu, "authors": get_authors(), "genres": list_genre}


# Create your views here.
def index(request):
    return render(request, 'library/index.html', context=data)


def about(request):
    return render(request, 'library/about.html', context=data)


def authors(request):
    return render(request, 'library/authors.html', context=data)


def genres(request):
    return render(request, 'library/genres.html', context=data)


def log_in(request):
    return render(request, 'library/log_in.html', context=data)


def book_by_id(request, IDBook):
    for book in books:
        if book["IDBook"] == IDBook:
            return render(request, 'library/book_by_id.html', context=book)
    raise Http404("Book not found")


def genre_by_id(request, IDGenre):
    books_by_genre = []
    genre_title = ""
    for genre in list_genre:
        if genre["id"] == IDGenre:
            genre_title = genre["title"]
            break


