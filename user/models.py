from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    userid = models.AutoField(primary_key=True)
    namalengkap = models.CharField(max_length=255)
    alamat = models.TextField()

    def __str__(self):
        return self.username