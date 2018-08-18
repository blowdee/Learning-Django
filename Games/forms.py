from django import forms

from Games.models import Studio, Genre, Game


class StudioForm(forms.ModelForm):
    name = forms.CharField(max_length=60)
    country = forms.CharField(max_length=40)

    class Meta:
        model = Studio
        fields = ('name', 'country')


class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=30)

    class Meta:
        model = Genre
        fields = ('name', )


class GameForm(forms.ModelForm):
    studio = forms.ModelChoiceField(Studio.objects.all())
    genre = forms.ModelChoiceField(Genre.objects.all())

    class Meta:
        model = Game
        fields = ('name', 'studio', 'genre')
