# Generated by Django 4.2 on 2024-06-12 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_arriendos', '0004_inmuebles_m2_construidos_inmuebles_m2_terreno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
