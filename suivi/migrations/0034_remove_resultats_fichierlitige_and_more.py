# Generated by Django 5.0.1 on 2024-08-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0033_remove_offres_ajt_remove_offres_asc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultats',
            name='fichierlitige',
        ),
        migrations.AddField(
            model_name='resultats',
            name='fichier_litige',
            field=models.FileField(blank=True, null=True, upload_to='litiges/'),
        ),
        migrations.AlterField(
            model_name='resultats',
            name='litige',
            field=models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], max_length=3, null=True),
        ),
    ]