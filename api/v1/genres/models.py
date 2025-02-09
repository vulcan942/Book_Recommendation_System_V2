from django.db import models


class Genre(models.Model):
    class Meta:
        db_table = "genres"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
