from django.db import models
from django.contrib.auth.models import User


class Comunity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    nickname = models.OneToOneField(User)
    nombre = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    comunity = models.ForeignKey(Comunity)
    options = ((1, 'Presidente'), (2, 'Auditor'))
    type_user = models.IntegerField(choices=options, default=1)

    def __str__(self):
        return self.nickname.username


class Activity(models.Model):
    comunity = models.ForeignKey(Comunity)
    fields = models.FileField(upload_to='archivos/')

    def __str__(self):
        return str(self.comunity)


class Nota(models.Model):
    comunity = models.ForeignKey(Comunity)
    activities = models.ForeignKey(Activity)
    puntuacion = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.comunity)