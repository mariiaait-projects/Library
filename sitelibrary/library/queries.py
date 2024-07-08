import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitelibrary.settings')
django.setup()

from library.models import Book

print(Book.objects.all().order_by('published_year'))
print(Book.objects.all())