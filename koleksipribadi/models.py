from django.db import models
from django.contrib.auth.models import User
from buku.models import Buku
from django.conf import settings

# Create your models here.
class Koleksipribadi(models.Model):
    koleksiid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bukuid = models.ForeignKey(Buku, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'koleksipribadi'

    def __str__(self):
        return f"{self.user}'s Collection: {self.buku.judul}"