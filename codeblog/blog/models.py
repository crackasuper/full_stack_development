from django.db import models

# Create your models here.

class blog(models.Model):
    sno = models.AutoField(primary_key= True)
    title = models.CharField(max_length = 40)
    content = models.CharField(max_length = 100)
    author = models.CharField(max_length = 30)
    slug = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.title + " " + self.author