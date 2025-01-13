from rest_framework import serializers
from .models import Film, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'comment', 'rating', 'film']

class FilmSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Nested serializer for reviews
    average_rating = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.get_average_rating() or 0  # Return 0 if no ratings

    def get_image_url(self, obj):
        if obj.image:
            try:
                return obj.image.url
            except Exception:
                return None
        return None

    class Meta:
        model = Film
        fields = ['id', 'name', 'genre', 'release_year', 'reviews', 'average_rating', 'image_url']
