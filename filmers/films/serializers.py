from rest_framework import serializers
from .models import Film, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'comment', 'rating', 'film']

class FilmSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Nested serializer for reviews

    class Meta:
        model = Film
        fields = ['id', 'name', 'genre', 'release_year', 'reviews']
