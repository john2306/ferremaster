# Generated by Django 2.2.3 on 2021-10-20 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='galeria',
            new_name='Proyecto',
        ),
        migrations.AlterModelOptions(
            name='proyecto',
            options={'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
    ]