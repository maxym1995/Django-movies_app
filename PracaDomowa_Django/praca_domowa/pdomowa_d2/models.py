from django.db import models

# Create your models here.
# from pdomowa_d2.models import *, from pdomowa_d2.scripts import *
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

class Genre(models.Model):
    name = models.CharField(max_length=32)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.PROTECT, null = True, related_name='+')
    screenplay = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, related_name='+')
    starring = models.ManyToManyField(Person)
    year = models.IntegerField(null=True)
    rating = models.DecimalField(decimal_places=1,max_digits=3)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.id}, {self.title}, {self.year}'

# p1 = Person.objects.create(first_name="Pawel",last_name='Malinowski')
# Person.objects.create(first_name="Jerzy",last_name='Brzeczek')
# Person.objects.create(first_name="Pawel",last_name='Malaszynski')
# Person.objects.create(first_name="Tommy",last_name='LeJones')
# Person.objects.create(first_name="Krzysztof",last_name='Ibisz')
# Person.objects.create(first_name="Damian",last_name='Gradek')
# Person.objects.create(first_name="Tomasz",last_name='Kot')

# Person.objects.create(first_name="Leszek",last_name='Ojrzynski')
# Person.objects.create(first_name="Jerzy",last_name='Kryszak')
# Person.objects.create(first_name="Piotr",last_name='Kasiasty')
# Person.objects.create(first_name="Ewa",last_name='Bdronicka')
# Genre.objects.create(name="Aktor")
# Genre.objects.create(name="Scenarzysta")
# Genre.objects.create(name="Rezyser")
# Genre.objects.create(name="Charakteryzator")
# Genre.objects.create(name="Producent")
#movies
# Movie.objects.create(title="Sami Swoi",director=Person[5],screenplay=Person[6],year=1990,rating=7.5)
# Movie.objects.create(title="",director=,screenplay=,starring=,year=,rating=,genre=)
# Movie.objects.create(title="",director=,screenplay=,starring=,year=,rating=,genre=)
# Movie.objects.create(title="",director=,screenplay=,starring=,year=,rating=,genre=)

# Song.objects.create(title='Hej Sokoly',duration = datetime.time(0,3,20), album = album[0])

# Movie.objects.create(title="Daleko od Szosy",director=Person.objects.get(id=1),screenplay=Person.objects.get(id=9),year=1985,rating=5.5)
# Movie.objects.create(title="Daleko od Szosy",director=Person.objects.get(id=1),screenplay=Person.objects.get(id=9),year=1985,rating=5.5)
# Movie.objects.create(title="Listy do M",director=Person.objects.get(id=3),screenplay=Person.objects.get(id=10),year=2004,rating=3.0)
# Movie.objects.create(title="Nawalnica",director=Person.objects.get(id=5),screenplay=Person.objects.get(id=10),year=2000,rating=10.0)
# Movie.objects.create(title="Onomatopeja",director=Person.objects.get(id=7),screenplay=Person.objects.get(id=11),year=2011,rating=5.5)
# m1 = Movie.objects.get(id=2)
# m2 = Movie.objects.get(id=3)
# m3 = Movie.objects.get(id=4)
# m4 = Movie.objects.get(id=5)
#
# m.genre.add(Genre.objects.get(id=4))
# m.genre.add(Genre.objects.get(id=3))
# m.genre.add(Genre.objects.get(id=2))
# m.genre.add(Genre.objects.get(id=1))