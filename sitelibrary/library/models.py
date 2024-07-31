# Create your models here.

from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author', through='BookAuthor')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True)
    published_year = models.IntegerField()
    ISBN = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ["published_year"]
        indexes = [models.Index(fields=["published_year"])]

class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.genre

class BookAuthor(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'author')

