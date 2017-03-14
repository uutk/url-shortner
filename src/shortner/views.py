from django.shortcuts import render, get_object_or_404 
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import ChotaURL
from .forms import SubmitURL
from analytics.models import ClickEvent
# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = SubmitURL()
		context = {
			"title" : "Chotu..!!!",
			"form" : form
		}
		return render(request, "shortner/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitURL(request.POST)
		context = {
			"title" : "Chotu..!!!",
			"form" : form
		}
		template = "shortner/home.html"
		
		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = ChotaURL.objects.get_or_create(url=new_url)
			context = {
				"object" : obj,
				"created" : created
			}
			if created:
				template = "shortner/created.html"
			else:
				template = "shortner/exists.html"
		
		return render(request, template, context)

class ChotuRedirectView(View):
	
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(ChotaURL, shortcode=shortcode)
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)