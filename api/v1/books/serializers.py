from rest_framework.serializers import ModelSerializer

from api.v1.authors.serializers import AuthorSerializer
from api.v1.genres.serializers import GenreSerializer
from .models import Book


class BookSerializer(ModelSerializer):
    author = AuthorSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "genres",
            "description",
            "rating",
            "image_url",
            "published_date",
        ]
