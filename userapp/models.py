from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class BlogUser(AbstractUser):
    nickname = models.CharField(verbose_name='昵称', max_length=20, default='')
