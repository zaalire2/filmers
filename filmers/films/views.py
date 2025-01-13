from rest_framework import generics
from .models import Film, Review
from .serializers import FilmSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated


class FilmListAPIView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

