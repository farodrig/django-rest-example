from rest_framework import serializers

from posts.models import Comment, Post


class PostSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Post
        fields = ['url', 'creator', 'title', 'body', 'created', 'modified']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'post', 'creator', 'body', 'created', 'modified']
