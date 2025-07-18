# Generated by Django 5.2.1 on 2025-05-20 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blocklogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('date_debut', models.DateField(null=True)),
                ('date_fin', models.DateField(null=True)),
                ('goal', models.TextField(null=True)),
                ('backlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprints', to='blocklogs.backlogs')),
            ],
        ),
    ]
