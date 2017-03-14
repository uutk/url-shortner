from django.shortcuts import render, get_object_or_404 
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import ChotaURL
# Create your views here.

class ChotuRedirectView(View):
	
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(ChotaURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)