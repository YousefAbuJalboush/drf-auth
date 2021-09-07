from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model

# Create your models here.

class Car(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)    
    modelCar = models.CharField(max_length=64)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.modelCar