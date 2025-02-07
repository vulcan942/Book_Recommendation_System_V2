from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']




class RegisterSerializer(serializers.ModelSerializer):
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "refresh", "access"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Ensures password is hashed
        refresh = RefreshToken.for_user(user)
        
        # Attach tokens to the response
        user.refresh = str(refresh)
        user.access = str(refresh.access_token)
        
        return user
