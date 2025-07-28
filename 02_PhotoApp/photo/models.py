from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    price = models.IntegerField()