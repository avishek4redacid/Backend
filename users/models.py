from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	first_name = models.CharField(max_length=50) 
	last_name = models.CharField(max_length=50) 
	company_name = models.CharField(max_length=50) 
	city = models.CharField(max_length=50) 
	state = models.CharField(max_length=50) 
	zip_code = models.CharField(max_length=50) 
	email = models.EmailField() 
	web = models.CharField(max_length=50) 
	age = models.CharField(max_length=50) 


	def __str__(self):
		return self.city


