from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Uživatel'
        verbose_name_plural = 'Uživatelé'
        ordering = ['username']

class Game(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Název')
    description = models.TextField(max_length=1000, verbose_name='Popis')
    release_date = models.DateField(verbose_name='Datum vydání')
    developer = models.CharField(max_length=100, verbose_name='Vývojář')
    publisher = models.CharField(max_length=100, verbose_name='Vydavatel')
    genres = models.ManyToManyField('Genre', related_name='games', verbose_name='Žánry')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hra'
        verbose_name_plural = 'Hry'
        ordering = ['title']

class Run(models.Model):
    PLATFORMS = [
        ('PC', 'PC'),
        ('PS4', 'PlayStation 4'),
        ('XBOX', 'Xbox One'),
        ('SWITCH', 'Nintendo Switch'),
        ('PS5', 'PlayStation 5'),
        ('XBOX_SERIES_X', 'Xbox Series X'),
    ]

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='speedruns', verbose_name='Hra')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='speedruns', verbose_name='Uživatel')
    time = models.DurationField(verbose_name='Čas')
    date = models.DateField(auto_now_add=True, verbose_name='Datum')
    platform = models.CharField(max_length=50, verbose_name='Platforma', choices=PLATFORMS)
    category = models.CharField(max_length=50, verbose_name='Kategorie')

    def __str__(self):
        return f"{self.user.username} - {self.game.title} - {self.time}"

    class Meta:
        verbose_name = 'Speedrun'
        verbose_name_plural = 'Speedruny'
        ordering = ['time']

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Název')
    description = models.TextField(blank=True, verbose_name='Popis')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'
        ordering = ['name']