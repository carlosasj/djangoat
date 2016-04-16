from django.shortcuts import render, redirect, render_to_response
from django.http import Http404
from django.template import RequestContext
import random

# Create your views here.

def index(request):
    return render(request, "game/index.html")


def game_ini(request):
    try:
        state = request.session['state']
    except KeyError:
        request.session['state'] = 'initial'
        state = request.session['state']

    if state == 'initial':
        request.session['prize'] = random.randrange(1,4)
        context = {
            'door1': 'closed',
            'door2': 'closed',
            'door3': 'closed',
        }

    elif state == 'choose':
        context = {
            'door1': 'closed',
            'door2': 'closed',
            'door3': 'closed',
            'user_choose': str(request.session['answer']),
            'presenter_choose': '',
        }
        id_door = ''.join(['door', str(request.session['answer'])])
        context[id_door] = 'choose'

        options = ['door1', 'door2', 'door3']
        options.pop(options.index(id_door))
        try:
            options.pop(options.index(''.join(['door', str(request.session['prize'])])))
        except:
            pass
        choice = random.choice(options)
        context[choice] = 'open'
        context['presenter_choose'] = choice[-1]

    elif state == 'confirmed_chose':
        context = request.session['previous_context']

        # change the options
        if request.session['answer'] == 'change':
            for key, value in context.items():
                if value == 'choose':
                    context[key] = 'closed'
                elif value == 'closed':
                    context[key] = 'choose'
        request.session['answer'] = 'same'
        context['result'] = 'right' if context['door'+str(request.session['prize'])] == 'choose' else 'wrong'

    else:
        context = {}

    request.session['previous_context'] = context
    return render(request, "game/game.html", context)


def game_answer(request, id):
    state = request.session['state']
    if state=='initial':
        # id = 1 -> Chose door 1
        # id = 2 -> Chose door 2
        # id = 3 -> Chose door 3
        if int(id) not in [1, 2, 3]:
            raise Http404
        request.session['answer'] = id
        request.session['state'] = 'choose'

    elif state=='choose':
        # id = 1 -> DON'T change the door
        # id = 2 -> CHANGE the door
        if int(id) not in [1, 2]:
            raise Http404
        request.session['answer'] = 'change' if int(id) == 2 else 'same'
        request.session['state'] = 'confirmed_chose'

    return redirect('game_ini')


def game_reset(request):
    request.session['state'] = 'initial'
    request.session['previous_context'] = {}
    return redirect('game_ini')


def bad_request(request):
    response = render_to_response(
        "bad_request.html",
        context_instance=RequestContext(request)
    )

    response.status_code = 400
    return response