from django.shortcuts import render
from .models import Post
from django.views import generic 
# Create your views here.


class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-date_of_event')
  template_name = 'index2.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'