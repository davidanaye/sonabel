# Generated by Django 5.0.1 on 2024-07-24 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0020_avis_date_lancement_pulication'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultats',
            name='lot',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resultat', to='suivi.lots'),
        ),
        migrations.AlterField(
            model_name='avis',
            name='date_publi',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de publication DGCMEF'),
        ),
    ]
