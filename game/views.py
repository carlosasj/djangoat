from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    return render(request, "game/index.html")


def game_ini(request):
    if not request.session['state']:
        request.session['state'] = 'initial'
    state = request.session['state']

    if state=='initial':
        request.session['goat'] = random.randrange(1,4)
        context = {
            'door1': 'closed',
            'door2': 'closed',
            'door3': 'closed',
        }

    elif state=='chosed':
        context = {
            'door1': 'closed',
            'door2': 'closed',
            'door3': 'closed',
        }
        id_door = ''.join('door', str(request.session['answer']))
        context[id_door] = 'chosed'

        options = ['door1', 'door2', 'door3']
        options.pop(options.index(id_door))
        try:
            options.pop(options.index(''.join('door', str(request.session['goat']))))
        except e:
            pass
        context[random.choice[options]] = 'open'


    return render(request, "game/game.html", context)


def game_answer(request, id):
    if state=='initial':
        request.session['state'] = 'chosed'
        request.session['answer'] = id

    return redirect('game_ini')