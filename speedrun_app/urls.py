from django.urls import path

from speedrun_app.views.user_view import CustomUserListView, CustomUserDetailView, CustomUserRegisterView, CustomUserLoginView, logout_view
from speedrun_app.views.game_view import GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView
from speedrun_app.views.genre_view import GenreListView, GenreCreateView, GenreUpdateView, GenreDeleteView
from speedrun_app.views.run_view import RunListView, RunDetailView, RunCreateView, RunUpdateView, RunDeleteView
from speedrun_app.views.about_view import AboutView


urlpatterns = [
    # URL patterns for user-related views
    path('users/', CustomUserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    path('users/register/', CustomUserRegisterView.as_view(), name='user_register'),
    path('users/login/', CustomUserLoginView.as_view(), name='user_login'),
    path('users/logout/', logout_view, name='user_logout'),

    # URL patterns for game-related views
    path('games/', GameListView.as_view(), name='game_list'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('games/create/', GameCreateView.as_view(), name='game_create'),
    path('games/<int:pk>/update/', GameUpdateView.as_view(), name='game_update'),
    path('games/<int:pk>/delete/', GameDeleteView.as_view(), name='game_delete'),

    # URL patterns for genre-related views
    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('genres/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genres/<int:pk>/update/', GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre_delete'),

    # URL patterns for run-related views
    path('runs/', RunListView.as_view(), name='run_list'),
    path('runs/<int:pk>/', RunDetailView.as_view(), name='run_detail'),
    path('runs/create/', RunCreateView.as_view(), name='run_create'),
    path('runs/<int:pk>/update/', RunUpdateView.as_view(), name='run_update'),
    path('runs/<int:pk>/delete/', RunDeleteView.as_view(), name='run_delete'),

    # URL patterns for about view
    path('about/', AboutView.as_view(), name='about'),
]