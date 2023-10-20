from django.db import models
from django.contrib.auth.models import User
 

class Community(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name 


class CommunityData(models.Model):
	community = models.ForeignKey(Community, on_delete=models.CASCADE)
	data_name = models.FileField(upload_to='data_files/')
	data_value = models.TextField()

	def __str__(self):
		return self.data_name.name