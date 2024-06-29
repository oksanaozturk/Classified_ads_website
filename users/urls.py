from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

app_name = UsersConfig.name
users_router = SimpleRouter()

# обратите внимание, что здесь в роуте мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")
"""
GET "users/" — список профилей пользователей
POST "users/" — регистрация пользователя
GET, PATCH, DELETE "users/{id}" — в соотвествии с REST и необходимыми permissions (для администратора)
GET PATCH "users/me" — получение и изменение своего профиля
POST "users/set_password" — ручка для изменения пароля
POST "users/reset_password" — ручка для направления ссылки сброса пароля на email*
POST "users/reset_password_confirm" — ручка для сброса своего пароля*
"""

urlpatterns = [
    path("", include(users_router.urls)),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]
