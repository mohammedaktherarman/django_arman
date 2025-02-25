# Generated by Django 5.1.5 on 2025-01-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('cognom', models.CharField(max_length=100)),
                ('cognom2', models.CharField(max_length=100)),
                ('correu', models.CharField(max_length=100)),
                ('curs', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('cognom', models.CharField(max_length=100)),
                ('cognom2', models.CharField(max_length=100)),
                ('correu', models.CharField(max_length=100)),
                ('curs', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=100)),
            ],
        ),
    ]
