from django.shortcuts import render, get_object_or_404, redirect

from Games.forms import GameForm, StudioForm, GenreForm
from Games.models import Game, Studio, Genre


def index(request):
    return render(request, 'index.html', {})


def games(request):
    result = Game.objects.all()
    return render(request, 'games.html', {'games': result})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game_detail.html', {'game': game})


def game_edit(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            game.studio = form.instance.studio
            game.genre = form.instance.genre
            game.save()
            return redirect('/games')
    else:
        form = GameForm(instance=game)
    return render(request, 'game_edit.html', {'form': form})


def game_delete(request, pk):
    Game.objects.filter(pk=pk).delete()
    return redirect('/games')


def new_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.studio = form.instance.studio
            game.genre = form.instance.genre
            game.save()
            return redirect('/games')
    else:
        form = GameForm()
    return render(request, 'game_edit.html', {'form': form})


def studios(request):
    result = Studio.objects.all()
    return render(request, 'studios.html', {'studios': result})


def studio_detail(request, pk):
    studio = get_object_or_404(Studio, pk=pk)
    return render(request, 'studio_detail.html', {'studio': studio})


def studio_edit(request, pk):
    studio = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = StudioForm(request.POST, instance=studio)
        if form.is_valid():
            studio = form.save(commit=False)
            studio.save()
            return redirect('/studios')
    else:
        form = GameForm(instance=studio)
    return render(request, 'studio_edit.html', {'form': form})


def studio_delete(request, pk):
    Studio.objects.filter(pk=pk).delete()
    return redirect('/studios')


def new_studio(request):
    if request.method == 'POST':
        form = StudioForm(request.POST)
        if form.is_valid():
            studio = form.save(commit=False)
            studio.save()
            return redirect('/studios')
    else:
        form = StudioForm()
    return render(request, 'studio_edit.html', {'form': form})


def genres(request):
    result = Genre.objects.all()
    return render(request, 'genres.html', {'genres': result})


def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return render(request, 'genre_detail.html', {'genre': genre})


def genre_edit(request, pk):
    genre = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            return redirect('/genres')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre_edit.html', {'form': form})


def genre_delete(request, pk):
    Genre.objects.filter(pk=pk).delete()
    return redirect('/genres')


def new_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            return redirect('/genres')
    else:
        form = GenreForm()
    return render(request, 'genre_edit.html', {'form': form})
