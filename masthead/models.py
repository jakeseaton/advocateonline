from django.db import models

class MastheadDis(models.Model):
	FALL = "FA"
	SPRING = "SP"
	SEMESTER_CHOICES = (
		(FALL, 'Fall'),
		(SPRING, 'Spring'),
	)
	semester = models.CharField(max_length=2, 
								choices=SEMESTER_CHOICES, 
								default=FALL)
	year_in_pos = models.IntegerField
	position = models.CharField(max_length=200)

class ExecName(models.Model):
	executive_name = models.CharField(max_length=200)