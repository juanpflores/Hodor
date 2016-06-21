from django.db import models

from places.models import (
    Region,
    Place
)


class Language(models.Model):

    name = models.CharField(max_length=250, unique=True)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name
        }


class Religion(models.Model):

    name = models.CharField(max_length=250, unique=True)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name
        }


class Culture(models.Model):

    ERAS = (
        ('ac', 'Antes de Cristo'),
        ('dc', 'Después de Cristo')
    )

    name = models.CharField(max_length=250, unique=True)
    region = models.ForeignKey(Region, blank=True)
    languages = models.ManyToManyField(Language)
    _year = models.PositiveIntegerField(default=1)
    _era = models.CharField(max_length=2, choices=ERAS)
    religion = models.ForeignKey(Religion, blank=True, null=True)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def establishment(self):
        return "{year} {era}".format(
            year=self._year,
            era=self._era
        )

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'region': self.region.name,
            'languages': self.languages,
            'religion': self.religion,
            'establishment': self.establishment
        }

    def __str__(self):
        return self.name


class God(models.Model):

    name = models.CharField(max_length=550, unique=True)
    culture = models.ForeignKey(Culture, blank=True, null=True)

    def __str__(self):
        return "{name} of {culture}".format(
            name=self.name,
            culture=self.culture.name
        )

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'culture': self.culture.name
        }


class Temple(models.Model):

    name = models.CharField(max_length=500)
    culture = models.ForeignKey(Culture)
    place = models.ForeignKey(Place)

    def __str__(self):
        return "Temple {name} of {culture} at {place}".format(
            name=self.name,
            culture=self.culture.name,
            place=self.place.name
        )

    def to_json(self):
        return {
            'id': self.pk,
            'culture': self.culture.name,
            'place': self.place.name
        }


class Museum(models.Model):

    name = models.CharField(max_length=500)
    cultures = models.ManyToManyField(Culture)
    place = models.ForeignKey(Place)

    def __str__(self):
        return "Museum: {name}".format(
            name=self.name,
        )

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'cultures': self.cultures,
            'place': self.place.name
        }
