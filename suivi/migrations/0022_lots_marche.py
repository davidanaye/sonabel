# Generated by Django 5.0.1 on 2024-07-24 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0021_resultats_lot_alter_avis_date_publi'),
    ]

    operations = [
        migrations.AddField(
            model_name='lots',
            name='marche',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lots', to='suivi.marches', verbose_name='Marché'),
        ),
    ]
