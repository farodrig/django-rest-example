from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    pass
