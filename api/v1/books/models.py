from django.db import models

from api.v1.authors.models import Author
from api.v1.genres.models import Genre


class Book(models.Model):
    class Meta:
        db_table = "books"

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")
    description = models.TextField()
    rating = models.FloatField(default=2.5)
    image_url = models.URLField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
