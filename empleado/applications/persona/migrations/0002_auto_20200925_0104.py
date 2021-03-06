# Generated by Django 3.1.1 on 2020-09-25 06:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Ingeniero'), ('4', 'Otro')], max_length=50, verbose_name='Trabajo'),
        ),
    ]
