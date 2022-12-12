# Generated by Django 4.1.4 on 2022-12-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, default=None, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('role', models.IntegerField(choices=[(0, 'employee'), (1, 'restaurant')], default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
