# Generated by Django 3.1.5 on 2021-01-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210126_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='release_date',
            field=models.DateField(verbose_name='Дата пересчета'),
        ),
    ]