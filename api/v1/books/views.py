from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related("author").prefetch_related("genres")
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related("author").prefetch_related("genres")
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
