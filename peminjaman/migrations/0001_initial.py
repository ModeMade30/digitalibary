# Generated by Django 3.0.5 on 2024-04-16 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buku', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('peminjamanid', models.AutoField(primary_key=True, serialize=False)),
                ('tanggalpeminjaman', models.DateField()),
                ('tanggalpengembalian', models.DateField()),
                ('statuspeminjaman', models.CharField(choices=[('Dipinjam', 'Dipinjam'), ('Dikembalikan', 'Dikembalikan')], max_length=50)),
                ('bukuid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='buku.Buku')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'peminjaman',
            },
        ),
    ]
