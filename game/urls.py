from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.index,
        name='index'
    ),
    url(
        r'^game/$',
        views.game_ini,
        name='game_ini'
    ),
    url(
        r'^game/answer/(\d+)/$',
        views.game_answer,
        name='game_answer'
    ),
    url(
        r'^game/reset/$',
        views.game_reset,
        name='game_reset'
    ),
    # url(
    #     r'^qrcode/(\d+)/$',
    #     qrcode,
    #     name='qrcode'
    # ),
]
