import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitelibrary.settings')
django.setup()

from library.models import Book

print(Book.objects.all().order_by('published_year'))
print(Book.objects.all())
#
# print(Book.objects.filter(genre = "Romance"))
#
# print(Book.objects.filter(published_year__gt=1950))
#
# print(Book.objects.filter(author = "Harper Lee"))
#
# print(Book.objects.get(ISBN = "9780345339683"))

# book = Book.objects.get(ISBN="9780345339683")
# book.title = "ROBOCOP"
# book.save()
print(Book.objects.filter(ISBN="9780345339683").update(title="ROBOCOP"))
