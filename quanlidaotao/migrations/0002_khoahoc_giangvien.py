# Generated by Django 3.2 on 2021-05-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanlidaotao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='khoahoc',
            name='giangvien',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
