from django.db import models
from django.utils import timezone


class Post(models.Model):
    nombre = models.CharField(max_length=200,default='ninguno')
    email = models.CharField(max_length=200)
    text = models.TextField(default='ninguno')

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Gato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    foto = models.CharField(max_length=200)

    def publish(self):
        self.save()

class Articulo(models.Model):
    autor = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    texto = models.TextField(max_length=500)
    foto = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.save()