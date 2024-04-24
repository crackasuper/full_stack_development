from typing import Any
from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
from django.utils.deconstruct import deconstructible

class GenerateProfileImagePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'media/accounts/{instance.user.id}/images/'
        name = f'profile_image.{ext}'
        return os.path.join(path, name)
user_profile_image_path = GenerateProfileImagePath()
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FieldFile(upload_to= user_profile_image_path, blank = True, null = True)
    
    