from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from posts.serializers import PostSerializer

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'created', 'modified', 'posts', 'comments']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
