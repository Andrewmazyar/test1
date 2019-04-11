# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField(
        max_length= 55,
        blank= False,
        verbose_name='enter_groups_name'
    )

    description = models.TextField(
        blank=False,
        verbose_name="enter_description_of_group"
    )

#    user = models.ManyToManyField(
 #       to = User
  #  )
