# Generated by Django 4.2.6 on 2023-10-21 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis_crud', '0003_pelicula_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]