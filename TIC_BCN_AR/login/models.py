from django.db import models

class Login(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    cognom = models.CharField(max_length=50)
    cognom2 = models.CharField(max_length=50)
