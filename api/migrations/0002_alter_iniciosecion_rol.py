# Generated by Django 5.2.1 on 2025-07-06 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iniciosecion',
            name='rol',
            field=models.CharField(choices=[('Agricultor', 'Agricultor'), ('Administrador', 'Administrador'), ('operador', 'Operador')], default='Seleccione su rol', max_length=20),
        ),
    ]
