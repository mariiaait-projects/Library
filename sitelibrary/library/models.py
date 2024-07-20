# Create your models here.

from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
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
