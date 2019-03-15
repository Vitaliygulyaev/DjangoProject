from django.db import models

class PeopleInf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    tel_number = models.CharField(max_length=11)
objects = PeopleInf()

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    login = models.TextField(max_length=10)
    password = models.CharField(min_length=8, max_length=15)
    



