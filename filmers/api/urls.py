from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
)
from films.views import FilmListAPIView, ReviewCreateAPIView

app_name = 'api'

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User endpoints
    path('user/profile/', UserProfileView.as_view(), name='user_profile'),
    
    # Film endpoints
    path('films/', FilmListAPIView.as_view(), name='film_list'),
    path('reviews/create/', ReviewCreateAPIView.as_view(), name='review_create'),
] 