from django.urls import path
# Используем SimpleRouter так как с ним можно создать несколько экземпляров класса, а с DefaultRouter только один
from rest_framework.routers import SimpleRouter

from main.apps import MainConfig
from main.views import AdViewSet, CommentViewSet, MyListAPIView

app_name = MainConfig.name
# Создаем экземпляр класса SimpleRouter(), он обеспечивает маршрутизацию всех путей CRUD
router = SimpleRouter()
router.register("ads", AdViewSet, basename="ads")
"""
GET "/main/ads/" — список объявлений пользователей
POST "/main/ads/" — создание нового объявления пользователя
GET, PATCH, DELETE "/main/ads/{id}" — в соотвествии с REST и необходимыми permissions (для администратора)

GET "/main/comments/" — список комментариев пользователей
POST "/main/comments/" — создание нового комментария пользователя
GET, PATCH, DELETE "/main/comments/{id}" — в соотвествии с REST и необходимыми permissions (для администратора)
"""
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("mylist/", MyListAPIView.as_view(), name="mylist"),

] + router.urls
