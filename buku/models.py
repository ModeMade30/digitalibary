from django.db import models
from kategoribuku.models import Kategoribuku

# Create your models here.
class Buku(models.Model):
    kategoriid = models.ForeignKey(Kategoribuku, on_delete=models.SET_NULL, null=True)
    bukuid = models.AutoField(primary_key=True)
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    tahunterbit = models.IntegerField()
    tersedia = models.BooleanField(default=True)

    class Meta:
        db_table = 'buku'
        
    def __str__(self):
        return self.judul