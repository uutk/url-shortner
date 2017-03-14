from __future__ import unicode_literals
from django.db import models
#from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
from .utlis import get_shortcode,create_shortcode
from .validators import validate_url

class ChotaURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(ChotaURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

class ChotaURL(models.Model):

	url = models.CharField(max_length=220, unique=True, blank=False, null=False, validators=[validate_url])
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

	def get_short_url(self):
		url_path = reverse("scode", kwargs={'shortcode' : self.shortcode},host='www', scheme='http', port='8000')
		return url_path
