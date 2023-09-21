from django.db import models

# Create your models here.
class Funko(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    collection = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.CharField()
    link = models.CharField()


    def __str__(self):
        return self.name