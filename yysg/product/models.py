# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class product(models.Model):
	product_id = Models.CharField(maxlength=32)
	product_name = Models.CharField(maxlength=128)



	def __str__(self):
        return self.product_name


