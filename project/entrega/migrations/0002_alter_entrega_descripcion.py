# Generated by Django 4.2.7 on 2023-11-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
