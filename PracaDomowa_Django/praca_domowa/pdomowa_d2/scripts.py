from .models import Movie
import random
import datetime


def show_movie(movies):
    for movie in movies:
        print(movie.id, movie.title)
    return movies
