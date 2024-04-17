from django.db import models

# Create your models here.
class Kategoribuku(models.Model):
    kategoriid = models.AutoField(primary_key=True)
    namakategori = models.CharField(max_length=255)

    class Meta:
        db_table = 'kategoribuku'
        
    def __str__(self):
        return self.namakategori