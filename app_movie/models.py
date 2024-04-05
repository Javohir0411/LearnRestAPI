from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(max_length=500)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name_plural = 'Genres'
        verbose_name = 'Genre'
        db_table = 'genre'


class Movie(models.Model):
    movie_name = models.CharField(max_length=500)
    movie_year = models.IntegerField()
    movie_director = models.CharField(max_length=500)
    movie_rating = models.FloatField()
    movie_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movie_banner = models.ImageField(upload_to='movies/')
    movie_url = models.URLField()
    movie_descriptions = models.CharField(max_length=500)

    def __str__(self):
        return self.movie_name

    class Meta:
        verbose_name_plural = 'Movies'
        verbose_name = 'Movie'
        db_table = 'movie'
