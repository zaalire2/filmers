from django.contrib import admin
from .models import Film, Review

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'release_year', 'get_average_rating')
    list_filter = ('genre', 'release_year')
    search_fields = ('name', 'genre')
    ordering = ('-release_year',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('film', 'user', 'rating', 'comment')
    list_filter = ('rating', 'film')
    search_fields = ('film__name', 'user', 'comment')
