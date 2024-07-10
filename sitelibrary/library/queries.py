import os
import django
from django.template import Library
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitelibrary.settings')
django.setup()

from library.models import Book

# print(Book.objects.all().order_by('published_year'))
# print(Book.objects.all())
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
# print(Book.objects.filter(ISBN="9780345339683").update(title="ROBOCOP"))
#
# print(Book.objects.filter(author='Charlotte Bronte').update(genre='Mystery'))

# books = Book.objects.filter(published_year__lt=2000)
# for book in books:
#     book.genre = 'Классическая литература: ' + book.genre
#     book.save()

# ids = Book.objects.values_list('id', flat=True)
# print(ids)
# random_ids = random.sample(list(ids), 3)
# print(random_ids)
# for id in random_ids:
#     Book.objects.filter(id=id).update(genre='')

# Book.objects.filter(genre='').update(ISBN='UNKNOWN')

# import datetime
# Book.objects.filter(title__icontains='great').update(published_year=datetime.datetime.now().year)

