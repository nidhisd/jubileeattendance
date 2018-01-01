from django.db import models


# Create your models here.
class Participant(models.Model):

	name = models.CharField(max_length=255)
	participant_id = models.CharField(max_length=255)
	grade = models.CharField(max_length=255, null = True)

	def __str__(self):
		return self.name


class Attendance(models.Model):

	date_marked = models.DateTimeField()
	participant = models.ForeignKey(Participant)
	am_pm = models.CharField(max_length=2)

	def __str__(self):
		return self.participant.name + ' ' + self.date_marked + ' ' + self.am_pm



