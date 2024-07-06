from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.author}"