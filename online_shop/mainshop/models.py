from django.db import models

# Create your models here.
class Posts(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField()
	price = models.IntegerField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title
