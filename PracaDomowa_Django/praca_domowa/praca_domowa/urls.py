"""praca_domowa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pdomowa_d2 import views as pd


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', pd.movies),
    path('sorting_movies/', pd.movies_sorting),
    path('search-movie/', pd.search_movie),
    path('movie-details/<int:movie_id>', pd.movie_details),
    path('persons/', pd.persons),
    path('delete-movie/<int:movie_id>', pd.delete_movie),
    path('add_person/', pd.AddPerson.as_view()),
    path('edit_person/<int:person_id>', pd.edit_person.as_view()),
    path('edit_movie/<int:movie_id>', pd.edit_movie.as_view()),
    path('add_movie/', pd.add_movie.as_view()),
]


# urlpatterns += staticfiles_urlpatterns()