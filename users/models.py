# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from groups.models import Group
from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(
        max_length=20,
        blank=False,
        verbose_name= 'enter you nickname'
    )

    create = models.DateTimeField(
        auto_now= False
    )
    groups = models.ManyToManyField(
        to = Group
    )