from django.db import models

# Create your models here.
class Participant(models.Model):

	name = models.CharField(max_length=255)
	participant_id = models.CharField(max_length=255)
	email_id = models.EmailField()


class Attendance(models.Model):

	date_marked = models.DateField()
	participant_id = models.ForeignKey(Participant)
	am_pm = models.CharField(max_length=2)
	timestamp = models.DateTimeField()

class Honors(models.Model):

	participant_id = models.ForeignKey(Participant)
	points = models.IntegerField()


