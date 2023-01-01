from django.db import models
from froala_editor.fields import FroalaField
from main.models import Course
import os

class PostFileContent(models.Model):
	file = models.FileField(upload_to='materials/', null=True, blank=True)
	posted = models.DateTimeField(auto_now_add=True)
 
	class Meta:
		verbose_name_plural = "Materials"
		ordering = ['-posted']
  
	def __str__(self):
		return str(self.file)
        
	def file_name(self):
		return self.file.name

	def post_date(self):
		return self.datetime.strftime("%d-%b-%y, %I:%M %p")

	def delete(self, *args, **kwargs):
		self.file.delete()
		super().delete(*args, **kwargs)

class Page(models.Model):
	title = models.CharField(max_length=150)
	content = FroalaField()
	files = models.ManyToManyField(PostFileContent)
	course_code = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
 
	class Meta:
		verbose_name_plural = "Page"
		ordering = ['-title']
        
	def __str__(self):
		return str(self.title)

	def delete(self, *args, **kwargs):
		self.file.delete()
		super().delete(*args, **kwargs)
	
