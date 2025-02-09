from rest_framework.serializers import ModelSerializer
from .models import UserRating


class UserRatingSerializer(ModelSerializer):
    class Meta:
        model = UserRating
        fields = "__all__"
