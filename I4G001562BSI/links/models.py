from django.db import models
from . import utils 
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Link(models.Model):
	target_url = models.URLField()
	description = models.CharField(max_length=200)
	identifier = models.SlugField(max_length=20, blank=True, unique=True) 
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	created_date = models.DateTimeField(null=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.identifier}"

	def save(self, *args, **kwargs):
		if not self.identifier:
			random_id = utils.generate_random_id()

	        # Make sure there is no other Link with that same ID
			while Link.objects.filter(identifier=random_id).exists():
				random_id = utils.generate_random_id()

			self.identifier = random_id

		# Complete the save operation   
		super().save(*args, **kwargs)        
