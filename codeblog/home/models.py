from datetime import datetime
from django.db import models
from django.utils.timezone import now
# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)
    content = models.TextField()

    
    def __str__(self) -> str:
        return self.name
    
class Signup(models.Model):
    username = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    phone = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    


    def __str__(self) -> str:
        return f'{self.username} - {self.email}'
    
class register(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    def __str__(self) -> str:
        return f'{self.username} - {self.email}'

    
