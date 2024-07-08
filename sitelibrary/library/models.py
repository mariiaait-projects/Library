# Create your models here.

from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ["published_year"]
        indexes = [models.Index(fields=["published_year"])]