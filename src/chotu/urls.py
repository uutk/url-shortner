from django.conf.urls import url
from django.contrib import admin
from shortner.views import ChotuRedirectView, HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', ChotuRedirectView.as_view(), name='scode'),
]
