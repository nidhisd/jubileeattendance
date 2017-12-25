from django.db import models

# Create your models here.
class Attendance(models.Model):

 	attendance_date = models.DateTimeField('Attendance date')

 	def __str__(self):
 		return self.username