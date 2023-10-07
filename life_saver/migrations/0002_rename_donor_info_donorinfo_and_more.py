# Generated by Django 4.1.11 on 2023-09-27 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('life_saver', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='donor_info',
            new_name='DonorInfo',
        ),
        migrations.AlterField(
            model_name='donorinfo',
            name='blood_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='life_saver.bloodgroup'),
        ),
        migrations.AlterModelTable(
            name='bloodgroup',
            table='db_blood_group',
        ),
        migrations.AlterModelTable(
            name='donorinfo',
            table='db_donor_info',
        ),
    ]