# Generated by Django 5.0.1 on 2024-10-18 22:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0036_remove_planitems_budget_travaux_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgets',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='budgets',
            name='libelle',
        ),
        migrations.RemoveField(
            model_name='budgets',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='devises',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='devises',
            name='libelle',
        ),
        migrations.RemoveField(
            model_name='devises',
            name='symbole',
        ),
        migrations.RemoveField(
            model_name='devises',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='modes',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='modes',
            name='description',
        ),
        migrations.RemoveField(
            model_name='modes',
            name='libelle',
        ),
        migrations.RemoveField(
            model_name='modes',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='status',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='status',
            name='libelle',
        ),
        migrations.RemoveField(
            model_name='status',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='budgets',
            name='nom',
            field=models.CharField(default='nom', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devises',
            name='nom',
            field=models.CharField(default='nom', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modes',
            name='nom',
            field=models.CharField(default='nom', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='nom',
            field=models.CharField(default='nom', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avis',
            name='date_lancement_pulication',
            field=models.DateField(default='2012-12-12', verbose_name='Date de lancement de publication'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avis',
            name='date_publi',
            field=models.DateTimeField(default='2012-12-12', verbose_name='Date de publication DGCMEF'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avis',
            name='num_publi',
            field=models.CharField(default=1, max_length=200, verbose_name='Numero de publication'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='date_retour_dgcmef',
            field=models.DateField(default='2012-12-12', verbose_name='Date retour la DGCMEF'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='date_retour_sign',
            field=models.DateField(default='2012-12-12', verbose_name='Date retour'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='date_trans_dgcmef',
            field=models.DateField(default='2012-12-12', verbose_name='Date de transmission à la DGCMEF'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='date_trans_sign',
            field=models.DateField(default='2012-12-12', verbose_name='Date envois pour signature'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='intitule_doss',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='numero_doss',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propriétaire'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marches',
            name='date_notif',
            field=models.DateField(default='2012-12-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marches',
            name='date_retour_sign',
            field=models.DateField(default='2012-12-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marches',
            name='montant',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marches',
            name='num_ref',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offres',
            name='date_prevu_reception',
            field=models.DateField(default='2012-12-12', verbose_name='Date prévue de réception des offres'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultats',
            name='date_prevu_pub',
            field=models.DateField(default='2012-12-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultats',
            name='litige',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultats',
            name='lot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='resultats', to='suivi.lots'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultats',
            name='statut',
            field=models.CharField(choices=[('Retenu', 'Retenu'), ('Non Retenu', 'Non Retenu')], default='oui', max_length=10),
            preserve_default=False,
        ),
    ]