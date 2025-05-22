from django.db import models
from django.utils import timezone


class Incident(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активний'),
        ('closed', 'Закритий'),
    ]

    title = models.CharField(max_length=200, verbose_name='Назва інциденту')
    latitude = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, verbose_name='Довгота')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Час створення')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Інцидент'
        verbose_name_plural = 'Інциденти'
        ordering = ['-created_at']