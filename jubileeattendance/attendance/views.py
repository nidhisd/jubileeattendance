from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
# Create your views here.
from .models import Participant, Attendance, Honors


def index(request):
	latest_attendance = Attendance.objects.order_by('-date_marked')[:10]
	template = loader.get_template('attendance/index.html')
	context = RequestContext(request, {
		'latest_attendance':latest_attendance
		})
	return HttpResponse(template.render(context))


def markedattendance(request, participant_id):
	latest_attendance = Attendance.objects.order_by('-date_marked')[:10]
	output = ",".join(q.date_marked for q in latest_attendance)
	return HttpResponse("Congrats %s you have marked attendance!!" % participant_id)


def showattendance(request, participant_id):
	return HttpResponse("Hi, %s You attended Khane on following days! Good job!" % participant_id)

def leadershipboard(request):
	return HttpResponse("These are the highest scorers!!")
