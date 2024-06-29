from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
    Класс сериализатора при регистрации Пользователя (модель User).
    """

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = "__all__"


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для текущего отображения Пользователя (модель User).
    """

    class Meta:
        model = User
        fields = (
            "email",
            "role",
            "first_name",
            "last_name",
            "password",
            "phone_number",
            "avatar",
        )
