from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название игры")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        return self.title

class GameSession(models.Model):
    """Модель для записи игровой сессии"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name='sessions'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name="Игра",
        related_name='sessions'
    )
    date = models.DateField(
        verbose_name="Дата сессии",
        help_text="Когда играли"
    )
    content = models.TextField(
        verbose_name="Что сделано",
        help_text="Подробное описание сессии"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Игровая сессия"
        verbose_name_plural = "Игровые сессии"
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['game']),
        ]

    def __str__(self):
        return f"{self.date} - {self.game.title}"
