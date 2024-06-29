from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    # Количество сущностей, которое будет выведено на 1 странице
    page_size = 4
    # Для самостоятельного выбора Пользователем количества сущностей на страницу
    page_size_query_param = 'page_size'
