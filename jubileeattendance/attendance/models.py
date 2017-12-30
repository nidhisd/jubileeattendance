from django.db import models


# Create your models here.
class Participant(models.Model):

	name = models.CharField(max_length=255)
	participant_id = models.CharField(max_length=255)
	email_id = models.EmailField()

	def __str__(self):
		return self.name


class Attendance(models.Model):

	date_marked = models.DateTimeField()
	participant_id = models.ForeignKey(Participant)
	am_pm = models.CharField(max_length=2)

class Honors(models.Model):

	participant_id = models.ForeignKey(Participant)
	points = models.IntegerField()


