# Generated by Django 2.0.7 on 2018-11-22 22:50

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('rutEmpresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=20)),
                ('longitud', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(default=core.models.get_default_my_hour, max_length=50)),
                ('registro', models.CharField(max_length=20)),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Colaborador')),
            ],
        ),
    ]
