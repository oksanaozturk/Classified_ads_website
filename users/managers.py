from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Функция создания пользователя — в нее мы передаем обязательные поля.
    """

    def create_user(
        self, email, first_name, last_name, phone_number, role="user", password=None
    ):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            role=role,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, email, first_name, last_name, phone_number, role="admin", password=None
    ):
        """
        Функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
