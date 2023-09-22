from django.db import models
from django.urls import reverse

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
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'funko_id': self.id})
    
class Buyer(models.Model):
    name = models.CharField()
    offer = models.FloatField(default=0.00)

    funko = models.ForeignKey(Funko, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is offering ${self.offer}'
    
    class Meta:
        ordering = ['offer']