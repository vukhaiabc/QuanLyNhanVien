# Generated by Django 3.2 on 2021-05-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ungdung', '0005_auto_20210509_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chucvu',
            name='mo_ta',
            field=models.TextField(blank=True, default=''),
        ),
    ]
