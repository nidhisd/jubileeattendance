from django.contrib import admin

# Register your models here.
from .models import Participant, Attendance
admin.site.register(Participant)
admin.site.register(Attendance)