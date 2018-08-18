from django.conf.urls import url
from django.contrib import admin

from Games import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/$', views.games, name='games'),
    url(r'^game/(?P<pk>[0-9]+)/$', views.game_detail, name='game_detail'),
    url(r'^game/new/$', views.new_game, name='new_game'),
    url(r'^game/(?P<pk>[0-9]+)/edit/$', views.game_edit, name='game_edit'),
    url(r'^game/(?P<pk>[0-9]+)/delete/$', views.game_delete, name='game_delete'),

    url(r'^studios/$', views.studios, name='studios'),
    url(r'^studio/(?P<pk>[0-9]+)/$', views.studio_detail, name='studio_detail'),
    url(r'^studio/new/$', views.new_studio, name='new_studio'),
    url(r'^studio/(?P<pk>[0-9]+)/edit/$', views.game_edit, name='studio_edit'),
    url(r'^studio/(?P<pk>[0-9]+)/delete/$', views.studio_delete, name='studio_delete'),

    url(r'^genres/$', views.genres, name='genres'),
    url(r'^genre/new/$', views.new_genre, name='new_genre'),
    url(r'^genre/(?P<pk>[0-9]+)/$', views.genre_detail, name='genre_detail'),
    url(r'^genre/(?P<pk>[0-9]+)/edit/$', views.game_edit, name='genre_edit'),
    url(r'^genre/(?P<pk>[0-9]+)/delete/$', views.genre_delete, name='genre_delete'),

    url(r'^admin/', admin.site.urls),
]