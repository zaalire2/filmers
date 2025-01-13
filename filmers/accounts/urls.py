from django.urls import path
from .views import (
    LoginAPIView,
    SignupAPIView,
    LogoutView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # API views only
    path('login/', LoginAPIView.as_view(), name="api_login"),
    path('signup/', SignupAPIView.as_view(), name="api_signup"),
    path('logout/', LogoutView.as_view(), name="api_logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
