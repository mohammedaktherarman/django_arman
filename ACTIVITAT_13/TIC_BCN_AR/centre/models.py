from django.db import models

from django.db import models

class student(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)
    correu = models.CharField(max_length=100)
    curs = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

class teacher(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)
    correu = models.CharField(max_length=100)
    curs = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

