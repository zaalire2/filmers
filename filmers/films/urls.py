from django.urls import path
from .views import FilmListAPIView, ReviewCreateAPIView

urlpatterns = [
    path('films/', FilmListAPIView.as_view(), name='film-list'),
    path('reviews/add/', ReviewCreateAPIView.as_view(), name='review-add'),
]