from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='post-detail'
    )

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'created', 'modified', 'posts']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', 'created', 'modified']
