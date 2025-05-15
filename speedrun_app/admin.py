from django.contrib import admin
from speedrun_app.models import CustomUser, Game, Run, Genre


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'developer', 'publisher')
    search_fields = ('title', 'developer', 'publisher')
    list_filter = ('release_date',)
    ordering = ('title',)

class SpeedrunAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'time', 'date', 'platform', 'category')
    search_fields = ('user__username', 'game__title', 'platform', 'category')
    list_filter = ('date', 'platform', 'category')
    ordering = ('-date',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Run, SpeedrunAdmin)
admin.site.register(Genre, GenreAdmin)

