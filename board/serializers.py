from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'cnt', 'content_at', 'use_yn', 'updated_at', 'created_at']
