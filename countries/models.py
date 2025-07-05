from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)
    languages = models.ManyToManyField('Language')

    def __str__(self):
        return self.name


