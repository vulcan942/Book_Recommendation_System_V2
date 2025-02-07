from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book, Author, Genre, UserRating
from .serializers import (
    BookSerializer,
    AuthorSerializer,
    GenreSerializer,
    UserRatingSerializer,
)


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related("author").prefetch_related("genres")
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related("author").prefetch_related("genres")
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer


class UserRatingListCreateView(generics.ListCreateAPIView):
    queryset = UserRating.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRatingSerializer


class UserRatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRating.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRatingSerializer
