from django.contrib import admin

from main.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Класс для регистрации модели Ad в Админке."""

    list_display = (
        "id",
        "title",
        "price",
        "description",
        "author",
        "created_at",
        "image",
    )
    list_filter = ("created_at",)
    search_fields = ("title", "author")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Класс для регистрации модели Comment в Админке."""

    list_display = (
        "id",
        "text",
        "author",
        "ad",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = ("ad", "author")
