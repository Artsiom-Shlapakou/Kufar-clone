from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from locations.models import Country, City

# Create your models here.

def get_user_photo_path(instance, filename):
    return "photos/{}/{}".format(instance.username, filename)


        
class User(AbstractBaseUser):

    photo = models.ImageField(
        upload_to=get_user_photo_path, null=True, blank=True
    )
    birthday = models.DateField()
  
    def get_location(self):
        return self.city, self.city.country,