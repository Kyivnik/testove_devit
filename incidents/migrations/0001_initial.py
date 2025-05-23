# Generated by Django 5.2.1 on 2025-05-22 16:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва інциденту')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11, verbose_name='Довгота')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Час створення')),
                ('status', models.CharField(choices=[('active', 'Активний'), ('closed', 'Закритий')], default='active', max_length=10, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Інцидент',
                'verbose_name_plural': 'Інциденти',
                'ordering': ['-created_at'],
            },
        ),
    ]
