from __future__ import unicode_literals
from django.db import models
from .utlis import get_shortcode,create_shortcode

class ChotaURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(ChotaURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

class ChotaURL(models.Model):

	url = models.CharField(max_length=220, unique=True, blank=False, null=False)
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	timestamp = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	objects = ChotaURLManager() #over writing default model manager

	#over writing default save method
	def save(self,*args,**kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(ChotaURL, self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)