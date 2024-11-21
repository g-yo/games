from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game, name='game'),
    path('racing/', views.racing_game, name='racing_game'),
    path('snake/', views.snake_game, name='snake_game'),
    path('race/', views.race_game, name='race_game'),
    path('bubble/', views.bubble_game, name='bubble_game'),

]

