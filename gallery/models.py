from ast import mod
from statistics import mode

from django.db import models


# Create your models here.
class Item(models.Model):
    title: str = models.CharField(max_length=100)
    description: str = models.TextField()
    url: str = models.URLField(blank=True)
    is_enabled: bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
