from enum import Enum

from django.db import models


class Sets(models.Model):
    set_name = models.CharField(null=False, unique=True, max_length=255)
    set_code = models.CharField(primary_key=True, max_length=10)
    max_cards = models.IntegerField(null=False)


class Cards(models.Model):
    set_code = models.ForeignKey(Sets, on_delete=models.CASCADE)
    card_number = models.TextField(null=False)
    card_name = models.TextField(null=False)
    quantity_normal = models.IntegerField(null=True, default=0)
    quantity_reverse = models.IntegerField(null=True, default=0)
    quantity_holo = models.IntegerField(null=True, default=0)
