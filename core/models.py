from django.db import models

class Compra(models.Model):
    item = models.CharField(
        'item',
        default=None,
        max_length=255,
        null=False,
        blank=False
    )

