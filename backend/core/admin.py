from django.contrib import admin

# Register your models here.
from .models import Game, GameSession


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at',)


@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'game', 'user', 'get_preview')
    list_filter = ('date', 'game', 'user')
    search_fields = ('content', 'game__title')
    date_hierarchy = 'date'

    def get_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    get_preview.short_description = "Превью"