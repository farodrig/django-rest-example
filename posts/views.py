from rest_framework import permissions, viewsets

from posts.models import Comment, Post

from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
