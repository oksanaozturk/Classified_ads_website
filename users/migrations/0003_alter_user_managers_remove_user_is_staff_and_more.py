# Generated by Django 5.0.6 on 2024-06-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_avatar_user_phone_number_user_role_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_superuser",
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("admin", "admin"), ("user", "user")],
                default="user",
                max_length=50,
                verbose_name="Роль Пользователя",
            ),
        ),
    ]
