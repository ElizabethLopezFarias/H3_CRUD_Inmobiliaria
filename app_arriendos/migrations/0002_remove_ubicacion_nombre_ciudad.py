# Generated by Django 4.2 on 2024-06-05 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_arriendos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubicacion',
            name='nombre_ciudad',
        ),
    ]