from django.db import models

# Create your models here.

class Book(models.Model):
	
	title = models.CharField(max_length = 12)
	date = models.DateTimeField(auto_now_add = True)

