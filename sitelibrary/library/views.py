from django.shortcuts import render

books = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960,
        "genre": "Fiction",
        "ISBN": "978-0-06-112008-4"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949,
        "genre": "Dystopian",
        "ISBN": "978-0-452-28423-4"
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_year": 1813,
        "genre": "Romance",
        "ISBN": "978-0-19-953556-9"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "genre": "Tragedy",
        "ISBN": "978-0-7432-7356-5"
    },
    {
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "published_year": 1851,
        "genre": "Adventure",
        "ISBN": "978-0-14-243724-7"
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "published_year": 1869,
        "genre": "Historical Fiction",
        "ISBN": "978-0-19-923276-5"
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "published_year": 1951,
        "genre": "Fiction",
        "ISBN": "978-0-316-76948-0"
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "published_year": 1954,
        "genre": "Fantasy",
        "ISBN": "978-0-618-00222-8"
    },
    {
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "published_year": 1847,
        "genre": "Romance",
        "ISBN": "978-0-14-144114-6"
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "published_year": 1937,
        "genre": "Fantasy",
        "ISBN": "978-0-618-00221-1"
    }
]

menu = [{"title": "Home", "URL": "home"}, {"title": "About", "URL": "about"}, {"title": "Authors", "URL": "authors"},
        {"title": "Log in", "URL": "log_in"}]

data = {"books": books, "title": "Library", "menu": menu}
# Create your views here.
def index(request):
    return render(request, 'library/index.html', context=data)