from __future__ import unicode_literals

from django.db import models
from .utlis import get_shortcode,create_shortcode
class ChotaURL(models.Model):

	url = models.CharField(max_length=220, unique=True, blank=False, null=False)
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	timestamp = models.DateTimeField(auto_now=True)


	def save(self,*args,**kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(ChotaURL, self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)