from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ['title', 'header_image', 'body',
                  'author', 'category', 'author_username', 'category_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }

        }