from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from main.models import Ad, Comment
from main.paginators import CustomPagination
from main.permissions import IsAdminOrOwner
from main.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdViewSet(ModelViewSet):
    """
    Класс для настройки CRUD модели Ad с помощью метода ViewSet.
    Create, Update, Retrieve, Delete.
    """
    serializer_class = AdSerializer
    # Получаем все данне из БД
    queryset = Ad.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        """
        Метод получения сериализатора в зависимости от запроса
        (вывод всего списка или просмотр одного объекта).
        """

        if self.action == "retrieve":
            return AdDetailSerializer

        return AdSerializer

    def perform_create(self, serializer):
        """
        Метод для присоединения Автора объявления к объявлению.
        """
        ad = serializer.save()
        ad.author = self.request.user
        ad.save()

    def get_permissions(self):
        """
        Метод для проверки доступа к функцианалу сайта, в зависимости от роли Пользователя.
        """
        if self.action in ['create', 'retrieve']:
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ['destroy', 'partial_update', 'update']:
            self.permission_classes = (IsAdminOrOwner,)
        elif self.action == 'list':
            self.permission_classes = (AllowAny,)

        return super().get_permissions()


class CommentViewSet(ModelViewSet):
    """
    Класс для настройки CRUD модели Commend с помощью метода ViewSet.
    Create, Update, Retrieve, Delete.
    """
    serializer_class = CommentSerializer
    # Получаем все данне из БД
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """
        Метод для присоединения Автора комментария к комментарию.
        """
        comment = serializer.save()
        comment.author = self.request.user
        # comment.ad = Ad.objects.get(pk=self.kwargs["ad_pk"])
        comment.save()

    def get_queryset(self):
        """
        Получает отзывы для определенного объявления.
        """
        ad_id = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, id=ad_id)
        return ad.comments.all().order_by("created_at")

    def get_permissions(self):
        """
        Метод для проверки доступа к функцианалу сайта, в зависимости от роли Пользователя.
        """
        if self.action in ['create', 'list', 'retrieve']:
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ['destroy', 'partial_update', 'update']:
            self.permission_classes = (IsAdminOrOwner,)
        elif self.action == 'list':
            self.permission_classes = (AllowAny,)

        return super().get_permissions()


class MyListAPIView(generics.ListAPIView):
    """
    Класс для получения списока объявлений текущего пользователя.
    """

    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)
