# Generated by Django 3.2 on 2021-05-09 08:24

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ungdung', '0002_hangsanxuat_smartphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChucVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_cv', models.CharField(blank=True, max_length=50)),
                ('cong_viec', models.CharField(blank=True, max_length=254)),
                ('mo_ta', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='NhanVienql',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ungdung.user')),
                ('nam_kn', models.ImageField(blank=True, default=0, max_length=3, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('ungdung.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PhongBan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_pb', models.CharField(blank=True, max_length=50)),
                ('truongphong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ungdung.nhanvienql')),
            ],
        ),
    ]
