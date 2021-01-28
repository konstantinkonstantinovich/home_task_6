from django.db import models
# Create your models here.


class Country(models.Model):
    population = models.IntegerField(default=10)
    name_of_country = models.CharField(max_length=250)

    def __str__(self):
        return self.name_of_country


class City(models.Model):
    country = models.OneToOneField(Country,
                                   on_delete=models.CASCADE, primary_key=True)
    city_name = models.CharField(max_length=250)

    def __str__(self):
        return self.city_name


class Citizen(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.email


class Name(models.Model):
    citizen = models.ManyToManyField(Citizen)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
