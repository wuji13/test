# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class product(models.Model):
	product_id = models.CharField(max_length=32)
	product_name = models.CharField(max_length=128)



	#def __str__(self):
       # return self.product_name


