from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_posts',
        verbose_name='Пользователь'
    )
    
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="описание" 
    )
    image = models.ImageField(
        upload_to="post_images/",
        verbose_name="Фотография"
    )
    created = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"