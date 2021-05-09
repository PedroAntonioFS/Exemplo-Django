from django.db import models

# Create your models here.

class Compra(models.Model):
    item = models.CharField(
        'item',
        default=None,
        max_length=255,
        null=False,
        blank=False
    )

