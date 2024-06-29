from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Ad(models.Model):
    """
    Класс для Модели объявления.
    """

    title = models.CharField(
        max_length=150,
        verbose_name="Название товара",
        help_text="Напишите название товара",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена товара", help_text="Напишите цену товара"
    )
    description = models.TextField(
        verbose_name="Описание товара",
        max_length=500,
        **NULLABLE,
        help_text="Опишите товар",
    )
    author = models.ForeignKey(
        User,
        related_name="ads",
        on_delete=models.CASCADE,
        verbose_name="Автор объявления",
        **NULLABLE,
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата и время создания"
    )
    image = models.ImageField(
        upload_to="ads/", verbose_name="Изображение товара", **NULLABLE
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return f"У товара {self.title} - цена: {self.price}"


class Comment(models.Model):
    """
    Класс для Модели комментария.
    """

    text = models.TextField(
        verbose_name="Текст отзыва", help_text="Введите текст Вашего комментария"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name="Aвтор",
        **NULLABLE,
    )
    ad = models.ForeignKey(
        Ad, related_name="comments", on_delete=models.CASCADE, verbose_name="Объявление"
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата и время создания"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.author} к объявлению {self.ad} создан {self.created_at}"
