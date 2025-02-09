from .models import Genre
from .serializers import GenreSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer
