# characters/models.py
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    hit_points = models.IntegerField(default=10)
