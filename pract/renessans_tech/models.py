from django.db import models
import json
from django.urls import reverse
from django.utils.text import slugify

class Task(models.Model):
    mas_data = []
    nameTranslit = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    cashback = models.CharField(max_length=255)
    screen = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    proc = models.CharField(max_length=255)
    rom = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    cur_price = models.CharField(max_length=255)
    previous_price = models.IntegerField(null=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.nameTranslit}"

