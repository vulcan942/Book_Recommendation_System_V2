from rest_framework.serializers import ModelSerializer
from .models import Book, Author, Genre, UserRating


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class UserRatingSerializer(ModelSerializer):
    class Meta:
        model = UserRating
        fields = "__all__"


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
