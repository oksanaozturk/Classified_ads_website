from rest_framework import serializers
from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Класс-сериалайзер для объектов модели Comment.
    """
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    ad_title = serializers.CharField(source="ad.title", read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для объектов модели Ad.
    """
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для просмотра детальной информации по объявлению.
    """
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_email = serializers.CharField(source="author.email", read_only=True)
    author_phone_number = serializers.CharField(source="author.phone_number", read_only=True)

    count_comments_for_ad = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    @staticmethod
    def get_count_comments_for_ad(ad):
        """
        Метод для получения количества комментариев к объявлению.
        """

        return ad.comments.count()

    class Meta:
        model = Ad
        fields = '__all__'
