from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Party(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(Student, related_name='parties')

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=200)
    parties = models.ManyToManyField(Party, related_name='movies')

    def __str__(self):
        return self.name