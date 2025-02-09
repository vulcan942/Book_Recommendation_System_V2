from django.db import models
from django.contrib.auth.models import User
from api.v1.books.models import Book


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
