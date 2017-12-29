from django.conf.urls import url
from . import views
from .import models

urlpatterns = [

	url(r'^$', views.index, name = "index"),
	url(r'^(?P<participant_id>[A-B|0-9]+)/markedattendance$', views.markedattendance, name = "markedattendance"),
	url(r'^(?P<participant_id>[A-B|0-9]+)/showattendance$', views.showattendance, name = "showattendance"),
	url(r'^leadershipboard/$', views.leadershipboard, name = "leadershipboard"),
]