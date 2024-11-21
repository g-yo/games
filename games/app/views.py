from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def game(request):
    return render(request, 'game.html')
def racing_game(request):
    return render(request, 'games/toe.html')

# View for the Snake game
def snake_game(request):
    return render(request, 'games/snake.html')
def race_game(request):
    return render(request, 'games/race.html')
def bubble_game(request):
    return render(request, 'games/bubble.html')

