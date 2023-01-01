from django.db import models
from django.contrib.auth.models import User
from main.models import Course
from page.models import Page

STATUS = ((0, "Draft"),(2,"Archived"), (1, "Published"))

# Create your models here.

class Module(models.Model):
	title = models.CharField(max_length=150)
	pages = models.ManyToManyField(Page)
	course_code = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
	status = models.IntegerField(choices=STATUS, default=1)

        
	def __str__(self):
		return self.title