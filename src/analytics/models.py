from __future__ import unicode_literals
from django.db import models
from shortner.models import ChotaURL

class ClickEventManager(models.Manager):
	def create_event(self, instance):
		if isinstance(instance, ChotaURL):
			obj, created = self.get_or_create(chota_url=instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None	

class ClickEvent(models.Model):
	chota_url = models.OneToOneField(ChotaURL)
	count = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now=True)

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)