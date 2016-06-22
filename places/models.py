from django.db import models


class Country(models.Model):

    name = models.CharField(max_length=250)

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


class Region(models.Model):

    name = models.CharField(max_length=500, unique=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    description = models.TextField(default='')

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Region: {name}".format(name=self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country
        }


class Place(models.Model):

    name = models.CharField(max_length=500)
    region = models.ForeignKey(Region)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    description = models.TextField(default='')

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{place} at region: {region}".format(
            place=self.name,
            region=self.region
        )

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'region': self.region.name,
            'country': self.region.country.name
        }
