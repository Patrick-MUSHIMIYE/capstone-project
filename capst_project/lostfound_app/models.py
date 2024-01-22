# create models

from django.db import models
from django.utils import timezone

class upload_image(models.Model):
    first_name = models.CharField(max_length=254)
    second_name = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    tel = models.CharField(max_length=254)
    upload_images = models.ImageField(blank=True, null=True, upload_to='uploads')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.first_name} {self.second_name}'
    
