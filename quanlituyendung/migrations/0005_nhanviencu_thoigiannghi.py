# Generated by Django 3.2 on 2021-05-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanlituyendung', '0004_nhanviencu'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhanviencu',
            name='thoigiannghi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]