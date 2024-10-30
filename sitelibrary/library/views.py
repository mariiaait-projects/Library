from decimal import Decimal

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from library.models import Book, Genre, Author, BookAuthor, CartHeader, CartDetails, UserRole, Coupon
from library.forms import BookForm, GenreForm, AuthorForm, UserRegistrationForm, UserLoginForm, CouponApplyForm
from django.contrib.auth import authenticate, login, logout

menu = [{"title": "Home", "URL": "home"},
        {"title": "About", "URL": "about"},
        {"title": "Authors", "URL": "authors"},
        {"title": "Genres", "URL": "genres"}]

manage_menu = [{"title": "Create book", "URL": "create_book"},
               {"title": "Create genre", "URL": "create_genre"},
               {"title": "Create author", "URL": "create_author"}]

auth_menu = [{"title": "Registration", "URL": "register"},
             {"title": "Login", "URL": "login"}]


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


def book_by_id(request, id):
    book = get_object_or_404(Book, id=id)
    authors_ids = BookAuthor.objects.filter(book_id=book.id).values_list('author', flat=True)
    authors = Author.objects.filter(id__in=authors_ids)
    context = {'book': book, 'authors': authors}
    return render(request, 'library/book_by_id.html', context=context)


@login_required(login_url=settings.LOGIN_URL)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_by_id', id=book.id)
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', context={"form": form})


@login_required(login_url=settings.LOGIN_URL)
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


@login_required(login_url=settings.LOGIN_URL)
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home')


def genre_by_id(request, id):
    books = Book.objects.filter(genre_id=id)
    title = Genre.objects.get(id=id)
    context = {"title": title, "books": books}
    return render(request, 'library/genre_by_id.html', context=context)


@login_required(login_url=settings.LOGIN_URL)
def create_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genres')
    else:
        form = GenreForm()
    return render(request, 'library/genre_form.html', context={"form": form})


@login_required(login_url=settings.LOGIN_URL)
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


@login_required(login_url=settings.LOGIN_URL)
def delete_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    return redirect('genres')


def author_by_id(request, id):
    author = get_object_or_404(Author, id=id)
    books = Book.objects.filter(authors__id=author.id)
    context = {"title": author.name, "books": books}
    print(books)
    return render(request, 'library/author_by_id.html', context=context)


@login_required(login_url=settings.LOGIN_URL)
def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'library/author_form.html', context={"form": form})


@login_required(login_url=settings.LOGIN_URL)
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


@login_required(login_url=settings.LOGIN_URL)
def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('authors')


@login_required(login_url=settings.LOGIN_URL)
def buy_book(request, id):
    book = get_object_or_404(Book, id=id)
    cart_header, _ = CartHeader.objects.get_or_create(user_role=request.user.userrole)
    purchases = CartDetails.objects.filter(cart_header=cart_header, book=book)
    if purchases.exists():
        purchases.update(quantity=F('quantity') + 1)
    else:
        CartDetails.objects.create(cart_header=cart_header, book=book)
    return redirect('cart')


@login_required(login_url=settings.LOGIN_URL)
def get_cart(request):
    form = CouponApplyForm()
    code = None
    discount = 0

    if CartHeader.objects.filter(user_role=request.user.userrole).exists():
        cart_header = CartHeader.objects.get(user_role=request.user.userrole)
        purchases = CartDetails.objects.filter(cart_header=cart_header)
        if cart_header.coupon is not None:
            code = cart_header.coupon.name
            discount = cart_header.coupon.discount
        if purchases.exists():
            total_before = Decimal(sum(map(lambda purchase: purchase.book.price * purchase.quantity, purchases)))
            total = round(total_before - (total_before * Decimal(discount / 100)), 2)
            return render(request, 'library/cart.html', context={'title': "Cart", 'purchases': purchases,
                                                                 'total': total, 'form': form, "code": code})
    return render(request, 'library/cart.html', context={"form": form, "code": code})


@login_required(login_url=settings.LOGIN_URL)
def delete_product_from_cart(request, id):
    purchase = CartDetails.objects.get(id=id)
    purchase.delete()
    cart_header = CartHeader.objects.get(user_role=request.user.userrole)
    rest_purchases = CartDetails.objects.filter(cart_header=cart_header)
    if not rest_purchases.exists():
        cart_header.delete()
    return redirect('cart')


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserRole.objects.create(user=user)
            return redirect("login")
    else:
        form = UserRegistrationForm()
        return render(request, 'library/register_form.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
        return render(request, "library/login_form.html", {'form': form})


@login_required(login_url=settings.LOGIN_URL)
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url=settings.LOGIN_URL)
def apply_coupon(request):
    if CartHeader.objects.filter(user_role=request.user.userrole).exists():
        cart_header = CartHeader.objects.get(user_role=request.user.userrole)
        form = CouponApplyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get("coupon")
            coupon = get_object_or_404(Coupon, name=code)
            cart_header.coupon = coupon
            cart_header.save()
    return redirect('cart')


@login_required(login_url=settings.LOGIN_URL)
def delete_coupon(request):
    cart_header = CartHeader.objects.get(user_role=request.user.userrole)
    cart_header.coupon = None
    cart_header.save()
    return redirect('cart')


def search_book(request):
    query = request.GET.get("query")
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, "library/index.html", context={"books": books})


def filter_books(request):
    books = Book.objects.all()
    genre_id = request.GET.get("genre")
    if genre_id and genre_id.isdigit():
        books=books.filter(genre__id=int(genre_id))
    author_id = request.GET.get("author")
    if author_id and author_id.isdigit():
        books=books.filter(authors__id=int(author_id))
    price_from = request.GET.get("price_from", 0)
    price_to = request.GET.get("price_to", 100)
    books = books.filter(price__gte=price_from).filter(price__lte=price_to)
    sort_by = request.GET.get("sort_by")
    if sort_by == 'price_asc':
        books = books.order_by('price')
    if sort_by == 'price_desc':
        books = books.order_by('-price')
    return render(request, "library/index.html", context={"books": books})

def cart_update_quantity(request):
    print("Python")
    return JsonResponse({"success": True})