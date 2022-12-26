from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Draft"),(2,"Archived"), (1, "Published"))

class Post(models.Model):
  title =  models.CharField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  date_of_event = models.DateField()
  content =  models.TextField(max_length=45)
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-date_of_event']

  def __str__(self):
    return self.title
