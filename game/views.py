from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "game/index.html")

def game_ini(request):
    pass