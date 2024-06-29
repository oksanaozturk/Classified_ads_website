from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для регистрации User в админке."""

    list_display = (
        "id",
        "email",
        "is_active",
        "password",
        "first_name",
        "last_name",
        "phone_number",
        "avatar",
        "role",
    )
    list_filter = ("email",)
    search_fields = ("email", "last_name", "phone_number")
