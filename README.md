## Classified_ads_website
## Доска объявлений (backend)

Бэкенд-часть проекта предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- Создание superuser
- Созданы инструкции для API в вариантах в swagger и redoc
- Добавлены настройки для работы в Docker

### Используемые технологии:

 - Python
 - Django
 - PostgerSQL
 - Django REST framework
 - Docker
 - Djoser

<details>
<summary> Инструкция по развертыванию проекта</summary>


1) ### Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла env.sample

#### Добавьте секретный ключ Вашего проекта
SECRET_KEY=

#### Добавьте настройки для подключения к базе данных (ДБ должна быть создана)
 - POSTGRES_DB=
 - POSTGRES_USER=
 - POSTGRES_HOST=
 - POSTGRES_PORT=
 - POSTGRES_PASSWORD=

2) ### Используется виртуальное окружение - venv, зависимости записаны в файл requirements.txt
 - pip install -r requirements.txt

3) ### Перед запуском web-приложения создайте базу данных, создайте и примените миграции
 - python manage.py migrate

4) #### Используйте команду для создания суперпользователя.
 - python manage.py csu

5) #### Для загрузки данных из фикстур используйте команду
 - python manage.py loaddata fixtures.users.json
 - python manage.py loaddata fixtures.ads.json
 - python manage.py loaddata fixtures.comments.json

6) ### Команда для запуска Приложения: 
  - python manage.py runserver


</details>

<details>
<summary> Инструкция по запуску Docker</summary>

1) Установите DockerDesktop на Ваше устройство

2) После развертывания проекта, необходимо создать файл .env, в котором указать данные для переменных окружения. 
Переменные находятся в файле env_example

3) Используется виртуальное окружение - venv, зависимости записаны в файл requirements.txt

4) Соберите образ и запустите проект при помощи команды:
```
docker-compose up --build
```

5) Перейти в приложение Docker Desktop, где запустился наш проект и далее по ссылке подключения
```
http://0.0.0.0:8000/
```
6) Для завершения работы: вводим в консоли Pycharm команду для остановки всех контейнеров
```
docker-compose stop
```
7) Для очистки от всех неиспользуемых образов и контейнеров, используем команду
```
docker system prune -a
```

</details>

### Автор проекта https://github.com/oksanaozturk