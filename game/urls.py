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
    # url(
    #     r'^programacao/(\d+)/$',
    #     subevent_details,
    #     name='subevent_details'
    # ),
    # url(
    #     r'^vagas-nos-minicursos/$',
    #     courses_vacancies,
    #     name='courses_vacancies'
    # ),
    # url(
    #     r'^qrcode/(\d+)/$',
    #     qrcode,
    #     name='qrcode'
    # ),
]
