# Generated by Django 5.0.1 on 2024-07-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0025_offres_fournisseur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marches',
            name='montant',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]