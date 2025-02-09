from django.db import models


class Author(models.Model):
    class Meta:
        db_table = "authors"

    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
