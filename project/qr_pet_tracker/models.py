from django.db import models
from django.utils import timezone

# Create your models here.

class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image_owner = models.ImageField(upload_to='images_owner/')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pets_by_id_owner')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pets_by_owner')
    name = models.CharField(max_length=100)
    image_pet = models.ImageField(upload_to='images_pet/')
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    qr_code = models.ImageField(upload_to='qr_codes/')
    created_at = models.DateTimeField(default=timezone.now)  # Nuevo campo con valor por defecto