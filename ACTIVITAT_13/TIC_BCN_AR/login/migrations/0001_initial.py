# Generated by Django 5.1.6 on 2025-02-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('cognom', models.CharField(max_length=50)),
                ('cognom2', models.CharField(max_length=50)),
            ],
        ),
    ]
