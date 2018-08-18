from django.db import models


class Studio(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, )
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name + ' by ' + self.studio.name
