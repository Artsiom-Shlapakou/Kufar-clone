from django.db import models

# Create your models here.
class Country(models.Model):
    country_id = models.CharField(primary_key=True, unique=True, max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        verbose_name_plural = "Countries"


class City(models.Model):
    city_id = models.CharField(primary_key=True, unique=True, max_length=10)
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    parent_id = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} city, {}".format(self.name, self.country.name)
    
    class Meta:
        verbose_name_plural = 'Cities'