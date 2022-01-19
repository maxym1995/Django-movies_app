from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
import random
from pdomowa_d2.models import *
# Create your views here.


def movies(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        return render(request, "form.html", context={"movies": movies})


def movies_sorting(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        return render(request, "sorting_form.html", context={"movies": movies})
    if request.method =="POST":
        sorting_type = request.POST.get("sorting")
        if sorting_type == "default":
            movies = Movie.objects.all()
            request.session['sorted'] = 0
            return render(request, "sorting_form.html", context={"movies": movies})
        elif sorting_type =="rosnaco":
            request.session['sorted'] = 2
            movies = Movie.objects.all().order_by('year')
            return render(request, "sorting_form.html", context={"movies": movies})
        elif sorting_type =="malejaco":
            movies = Movie.objects.all().order_by('-year')
            request.session['sorted'] = 1
            return render(request, "sorting_form.html", context={"movies": movies})


def search_movie(request):
    if request.method =="GET":
        return render(request, "search_movie.html")

    elif request.method =="POST":
        pass

def movie_details(request,movie_id):
    m = Movie.objects.get(id=movie_id)
    title = m.title
    year = m.year
    director = m.director.first_name, m.director.last_name
    screenplay = m.screenplay.first_name, m.screenplay.last_name
    # starring = m.starring.first_name, m.starring.last_name
    rating = m.rating
    genres_list = []
    genres = m.genre.all()
    for gen in genres:
        genres_list.append(gen.name)
    answer = f"""<html>
                  <body>
                    <p>
                        Tytul filmu: {title},<br>
                        rok produkcji {year},<br>
                        rezyser: {director},<br>
                        scenarzysta: {screenplay},<br>
                        ocena: {rating} <br>
                        ocena: {rating} <br>
                        gwiazda glowna: starring <br>
                        pracownicy: {genres_list} <br>
                    </p>
                  </body>
                </html>"""
    return HttpResponse(answer)

def persons(request):
    persons = Person.objects.all().order_by('last_name')
    return render(request, "persons_form.html", context={"persons": persons})


def add_person(request, first_name, last_name):
    answer = ''
    return HttpResponse(answer)

# def edit_person(request, person_id):
#     person_names = Person.objects.get(id=person_id)
#     # return render(request, "edit_person.html", context={"person_names": person_names})
#     return render(request, "edit_person.html", context={"persons":persons})

class edit_person(View):
    def get(self, request, person_id):
        person_id = person_id
        person = Person.objects.get(id=person_id)
        return render(request, "edit_person.html", context={"person": person, "person_id":person_id})

    def post(self, request, person_id):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        person_id = request.POST.get("person_id")
        person_id = int(person_id)
        p = Person.objects.get(id=person_id)
        p.first_name = first_name
        p.last_name = last_name
        p.save()
        # return HttpResponse('Dodano osobe'), HttpResponseRedirect("/persons/") chcialbym wyswietlic info a potem przekierowac za 5 sekund
        return HttpResponseRedirect("/persons/")

class AddPerson(View):
    def get(self, request):
        return render(request, "add_person.html")

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        Person.objects.create(first_name=first_name, last_name=last_name)
        # return HttpResponse('Dodano osobe'), HttpResponseRedirect("/persons/") chcialbym wyswietlic info a potem przekierowac za 5 sekund
        return HttpResponseRedirect("/persons/")

class add_movie(View):
    def get(self, request):
        person = Person.objects.all()
        genre = Genre.objects.all()
        return render(request, "add_movie.html", context={"person":person, "genre":genre})

    def post(self, request):
        title = request.POST.get("title")
        year = int(request.POST.get("year"))
        director = request.POST.get("director")
        rating = request.POST.get("rating")
        screenplay = request.POST.get("screenplay")
        genre = request.POST.getlist("genre")
        m = Movie.objects.create(title=title, rating=rating, year = year, director = Person.objects.get(id=director), screenplay = Person.objects.get(id=screenplay) )
        for g in genre:
            m.genre.add(Genre.objects.get(id=g))
            m.save()
        # return HttpResponse('Dodano osobe'), HttpResponseRedirect("/persons/") chcialbym wyswietlic info a potem przekierowac za 5 sekund
        return HttpResponseRedirect("/movies/")

class edit_movie(View):
    def get(self, request, movie_id):
        movie_id = movie_id
        movie = Movie.objects.get(id=movie_id)
        persons = Person.objects.all()
        director = movie.director
        genres = movie.genre.all()
        genre = Genre.objects.all()

        return render(request, "edit_movie.html", context={"movie": movie, "movie_id":movie_id, "persons":persons, "genre":genre, "genres":genres})

    def post(self, request, person_id):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        person_id = request.POST.get("person_id")
        person_id = int(person_id)
        p = Person.objects.get(id=person_id)
        p.first_name = first_name
        p.last_name = last_name
        p.save()
        # return HttpResponse('Dodano osobe'), HttpResponseRedirect("/persons/") chcialbym wyswietlic info a potem przekierowac za 5 sekund
        return HttpResponseRedirect("/persons/")

def delete_movie(request, movie_id):
    if request.method=="GET":
        movie_id = movie_id
        movie = Movie.objects.get(id=movie_id)
        return render(request, "delete_movie.html", context={"movie": movie, "movie_id":movie_id})
    elif request.method=="POST":
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return HttpResponse('Film zostal usuniety')