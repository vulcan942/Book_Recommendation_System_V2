from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer
