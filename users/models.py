from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

NULLABLE = {"blank": True, "null": True}


class UserRoles(models.TextChoices):
    """
    Enum-класс для пользователя.
    """

    ADMIN = "admin", _("admin")
    USER = "user", _("user")


class User(AbstractUser):
    """Класс для создания модели Пользователя"""

    username = None

    email = models.EmailField(
        max_length=150, unique=True, verbose_name="email", help_text="Введите email"
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя Пользователя",
        help_text="Ввведите имя Пользователя",
        **NULLABLE,
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия Пользователя",
        **NULLABLE,
        help_text="Ввведите фамилию Пользователя",
    )

    # Необходимо добавить библиотеку через команду pip install "django-phonenumber-field[phonenumberslite]"
    phone_number = PhoneNumberField(
        verbose_name="Номер телефона",
        help_text="Укажите Ваш номер телефона",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users_avatar",
        verbose_name="Аватар пользователя",
        help_text="Загрузите изображение",
        **NULLABLE,
    )

    role = models.CharField(
        max_length=50,
        default="user",
        verbose_name="Роль Пользователя",
        choices=UserRoles.choices,
    )

    # Выбираем полем для авторизации email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "role"]

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    class Meta:
        verbose_name = "Пользоаптель"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Пользователь с {self.email} является {self.role}"
