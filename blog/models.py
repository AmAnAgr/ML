from django.db import models
import datetime
from django.utils.encoding import smart_text
import PIL as Pillow

# Create your models here.

class Image(models.Model):
	title = models.CharField(max_length=220)

	def __str__(self):
		return self.title

class Topic(models.Model):
	title		= models.CharField(max_length=220)
	description = models.TextField()

	def __str__(self):
		return smart_text(self.title)


class BlogPost(models.Model):
	title        = models.CharField(max_length=220)
	description  = models.TextField()
	publish_time = models.DateTimeField(default=datetime.datetime.now)
	topic        = models.ForeignKey(Topic)	
	image        = models.ManyToManyField(Image, null=True, blank=True)

	def __str__(self):
		return smart_text(self.title)
