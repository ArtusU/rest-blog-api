from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'thumbnail'
        )


class PostUpdateeSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'thumbnail'
        )