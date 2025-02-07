from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('register/', RegisterView.as_view(), name='register'),  # User registration
]
