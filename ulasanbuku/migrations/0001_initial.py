# Generated by Django 3.0.5 on 2024-04-16 15:26

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
            name='Ulasanbuku',
            fields=[
                ('ulasanid', models.AutoField(primary_key=True, serialize=False)),
                ('ulasan', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('bukuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='buku.Buku')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ulasanbuku',
            },
        ),
    ]
