# Generated by Django 5.1.7 on 2025-03-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_countrycodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('passwordHash', models.CharField(max_length=100)),
                ('salt', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='CountryCodes',
            new_name='CountryCode',
        ),
    ]
