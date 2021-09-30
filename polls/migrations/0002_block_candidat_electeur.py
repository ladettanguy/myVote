# Generated by Django 3.2.7 on 2021-09-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_block', models.IntegerField(default=0)),
                ('hashPrecedent', models.CharField(max_length=100)),
                ('actuel', models.CharField(max_length=100)),
                ('hashSuivant', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_candidat', models.IntegerField(default=0)),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=15)),
                ('parti', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Electeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_electeur', models.IntegerField(default=0)),
                ('token', models.CharField(max_length=10)),
            ],
        ),
    ]