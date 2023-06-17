from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_images/',
        verbose_name='Фотография профиля',
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"