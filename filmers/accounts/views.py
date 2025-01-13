from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model

User = get_user_model()

from django.core.mail import send_mail
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'accounts/login-signup.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

class LoginAPIView(TokenObtainPairView):
    pass

class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'accounts/login-signup.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('index')

class SignupAPIView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated]  
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'accounts/login-signup.html')

    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.pk}/{token}/"
            send_mail(
                'Password Reset',
                f'Click here to reset your password: {reset_url}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Password reset email sent')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'No user found with this email')
            return redirect('password_reset')