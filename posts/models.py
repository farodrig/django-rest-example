from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel

User = get_user_model()
class Post(TimeStampedModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=250)
    body = models.TextField()


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
