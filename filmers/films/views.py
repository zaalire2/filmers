from rest_framework import generics
from .models import Film, Review
from .serializers import FilmSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class FilmListAPIView(generics.ListAPIView):
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Film.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(genre__icontains=search_query)
            )
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

