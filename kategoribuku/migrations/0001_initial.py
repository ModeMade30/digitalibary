# Generated by Django 3.0.5 on 2024-04-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoribuku',
            fields=[
                ('kategoriid', models.AutoField(primary_key=True, serialize=False)),
                ('namakategori', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'kategoribuku',
            },
        ),
    ]
