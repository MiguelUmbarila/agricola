# Generated by Django 5.2.1 on 2025-06-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_admingestion_adminventario_gestiofechasadmin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminventario',
            name='CosechasRegistradas',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='adminventario',
            name='Semillas',
            field=models.CharField(choices=[('Alverja', 'Alverja'), ('Frijoles', 'Frijoles'), ('Cafe', 'Cafe'), ('Sandia', 'Sandia'), ('Papa', 'Papa'), ('Aguacate', 'Aguacate')], max_length=10),
        ),
        migrations.AlterField(
            model_name='cantidadproducto',
            name='cantidadesproducto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='semillatipo',
            name='tipo_semilla',
            field=models.CharField(choices=[('Alverja', 'Alverja'), ('Frijoles', 'Frijoles'), ('Cafe', 'Cafe'), ('Sandia', 'Sandia')], max_length=100),
        ),
    ]
