from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    class Meta:
        db_table = "genres"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    class Meta:
        db_table = "authors"

    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        db_table = "books"

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    image_url = models.URLField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class UserRating(models.Model):
    class Meta:
        db_table = "user_ratings"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="ratings")
    rating = models.FloatField()
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.rating})"
