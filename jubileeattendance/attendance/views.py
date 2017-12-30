from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
# import authentication library
from django.contrib.auth.decorators import login_required
# import time libraries
from django.utils import timezone
import datetime
# Create your views here.
from .models import Participant, Attendance, Honors
# import the logging library
import logging, sys

@login_required(login_url='/accounts/login/')
def index(request):
	return render(request, 'attendance/index.html')

@login_required(login_url='/accounts/login/')
def markedattendance(request):
	
	try:
	    participant = get_object_or_404(Participant, participant_id = request.POST['participant_id'])
	except:
		return render(request, 'attendance/marked.html', {'error_message': 'Please enter valid Participant ID'})
	else:
		current_date_time = timezone.localtime(timezone.now())
		print(timezone.localtime(timezone.now()), file = sys.stderr)
		def get_am_pm(cd):
			current_time = cd.time()
			morning_start = datetime.time(5, 0, 0)
			morning_end = datetime.time(8, 0, 0)
			evening_start = datetime.time(19, 0, 0)
			evening_end = datetime.time(22, 0, 0)
			if morning_start <= current_time <= morning_end:
				return 'am'
			elif evening_start <= current_time <= evening_end:
				return 'pm'
			else:
				return None
		
		def check_if_already_marked(participant, am_pm, cd):
			date_today = cd.date()
			return Attendance.objects.filter(
				date_marked__day = date_today.day,
				date_marked__month = date_today.month,
				date_marked__year = date_today.year,
				participant_id = participant,
				am_pm = am_pm).exists()

		def get_attendance_count(participant):
			morning_count = Attendance.objects.filter(participant_id = participant, am_pm = 'am').count()
			evening_count = Attendance.objects.filter(participant_id = participant, am_pm = 'pm').count()
			return (morning_count, evening_count)

		am_pm = get_am_pm(current_date_time)
		if not (am_pm is None):
			if not check_if_already_marked(participant, am_pm, current_date_time):
				Attendance.objects.create(date_marked = current_date_time, participant_id = participant, am_pm = am_pm)
				message = ('Hi %s your attendance have been marked!' % participant.name)
				morning_count, evening_count = get_attendance_count(participant)
				return render(request, 'attendance/marked.html',
					{'message': message,
					 'morning_count': morning_count,
					 'evening_count': evening_count})
			else:
				message = ('Hi %s your attendance has already been marked!' % participant.name)
				morning_count, evening_count = get_attendance_count(participant)
				return render(request, 'attendance/marked.html',
					{'message': message,
					 'morning_count': morning_count,
					 'evening_count': evening_count})

		else:
			error_message = ('Attendance can only be recorded between 5am - 8am and 7pm - 10pm!' 
				              ' Please contact Admin for any help!')
			return render(request, 'attendance/marked.html', {'error_message': error_message})


@login_required(login_url='/accounts/login/')
def showattendance(request, participant_id):
	return HttpResponse("Hi, %s You attended Khane on following days! Good job!" % participant_id)

@login_required(login_url='/accounts/login/')
def leadershipboard(request):
	return HttpResponse("These are the highest scorers!!")
