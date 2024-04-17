from django.db import models
from buku.models import Buku
from user.models import User

class Peminjaman(models.Model):
    DIPINJAM = 'Dipinjam'
    DIKEMBALIKAN = 'Dikembalikan'
    KONFIRMASI = 'Konfirmasi'

    STATUS_CHOICES = [
        (DIPINJAM, 'Dipinjam'),
        (DIKEMBALIKAN, 'Dikembalikan'),
        (KONFIRMASI, 'Konfirmasi'),
    ]

    peminjamanid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    bukuid = models.ForeignKey(Buku, on_delete=models.CASCADE, default=1)
    tanggalpeminjaman = models.DateField()
    tanggalpengembalian = models.DateField()
    statuspeminjaman = models.CharField(choices=STATUS_CHOICES, max_length=50)
    
    class Meta:
        db_table = 'peminjaman'