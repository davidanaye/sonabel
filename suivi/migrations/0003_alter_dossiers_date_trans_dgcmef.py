# Generated by Django 5.0.1 on 2024-05-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0002_dossiers_owner_alter_dossiers_planitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossiers',
            name='date_trans_dgcmef',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
