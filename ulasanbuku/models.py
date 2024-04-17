from django.db import models
from buku.models import Buku
from user.models import User

# Create your models here.
class Ulasanbuku(models.Model):
    ulasanid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    bukuid = models.ForeignKey(Buku, on_delete=models.SET_NULL, null=True)
    ulasan = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

    class Meta:
        db_table = 'ulasanbuku'

    def save(self, *args, **kwargs):
        if not self.ulasanid:
            last_id = Ulasanbuku.objects.order_by('ulasanid').last()
            if last_id:
                last_id_number = last_id.ulasanid + 1
            else:
                last_id_number = 1
            self.ulasanid = last_id_number
        super().save(*args, **kwargs)