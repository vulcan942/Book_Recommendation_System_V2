from rest_framework import generics
from .models import UserRating
from .serializers import UserRatingSerializer
from rest_framework.permissions import IsAuthenticated


class UserRatingListCreateView(generics.ListCreateAPIView):
    queryset = UserRating.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRatingSerializer


class UserRatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRating.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRatingSerializer
