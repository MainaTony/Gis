from django.db import models
from django.contrib.gis.db import models
#from django.contrib.gis.geos import GEOSGeometry
from django.db.models import Manager as GeoManager



#from django.contrib.gis.geos import Point
# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(null=True, blank=True)
    #location = models.CharField(max_length=20)
    #location = GEOSGeometry(srid=4326, null=True, blank=True)
    objects = GeoManager()
    #"GetMana
    #ger helps you to load the geospatial Model


    #Returning a name field forit  to be displayed on the django web page
    def __unicode__(self):
        return self.name

    #Ensuring that the plurals set by default in the django models is removed
    class Meta:
        verbose_name_plural="Incidences"
