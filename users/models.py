from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True)

    class Meta:
        # db_table = 'users'
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'

    def __str__(self) -> str:
        return self.username

