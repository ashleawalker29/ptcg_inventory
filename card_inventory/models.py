from enum import Enum

from django.db import models

class SetNames(Enum):
    BASE_SET = 'Base Set'

class CardTypes(Enum):
    GRASS = 'Grass'
    FIRE = 'Fire'
    WATER = 'Water'

class Cards(models.Model):
    set_name = models.CharField(max_length=5, choices=[(tag, tag.value) for tag in SetNames])
    card_number = models.TextField(null=False)
    card_name = models.TextField(null=False)
    card_type = models.CharField(max_length=5, choices=[(tag, tag.value) for tag in CardTypes])
    quantity_normal = models.IntegerField(null=True, default=0)
    quantity_reverse = models.IntegerField(null=True, default=0)
    quantity_holo = models.IntegerField(null=True, default=0)
